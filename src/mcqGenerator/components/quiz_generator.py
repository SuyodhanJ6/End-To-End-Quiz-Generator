import os, sys
import json
from typing import Optional

from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain.callbacks import get_openai_callback

from mcqGenerator.langchain import llm
# from mcqGenerator.config import RESPONSE_JSON
from mcqGenerator.constants import NUMBER, SUBJECT, TONE, DATA_FILE_PATH, MCQ_FILE_PATH
from mcqGenerator.config import RESPONSE_JSON, TEMPLATE, TEMPLATE2
from mcqGenerator.utils.main_utils import read_text_from_file, generate_quiz_table_data, write_quiz_data_to_csv

from mcqGenerator.logger import logging
from mcqGenerator.exception import McqGeneratorException

class QuizGeneratorEvaluator:
    """
    Class Name: QuizGeneratorEvaluator
    Description: Represents an evaluator for generating and analyzing multiple-choice quizzes.

    """

    def __init__(self, llm=llm, template=TEMPLATE, template2=TEMPLATE2, verbose=True):
        """
        Method Name: __init__
        Description: Initialize the QuizGeneratorEvaluator.

        Input:
        - llm: The language model instance.
        - template: The first template for the quiz generation.
        - template2: The second template for quiz evaluation.
        - verbose: Verbosity flag for logging.

        On Failure: Raises a McqGeneratorException in case of an initialization error.

        Version: 1.0
        """
        try:
            self.llm = llm
            self.template = template
            self.template2 = template2
            self.verbose = verbose
        except Exception as e:
            raise McqGeneratorException(e, sys)

    def quiz_generate_chain(self) -> Optional[LLMChain]:
        """
        Method Name: quiz_generate_chain
        Description: Initialize the quiz generation chain.

        Returns:
        - quiz_chain (LLMChain): Initialized LLMChain for quiz generation.

        On Failure: Raises a McqGeneratorException in case of an initialization error.

        Version: 1.0
        """
        try:
            logging.info("Initializing quiz generation chain...")
            quiz_generation_prompt = PromptTemplate(
                input_variables=["text", "number", "subject", "tone", "response_json"],
                template=self.template
            )

            quiz_chain = LLMChain(llm=self.llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=self.verbose)

            logging.info("Quiz generation chain initialized successfully.")
            return quiz_chain
        except Exception as e:
            raise McqGeneratorException(e, sys)

    def quiz_evaluate_chain(self) -> Optional[LLMChain]:
        """
        Method Name: quiz_evaluate_chain
        Description: Initialize the quiz evaluation chain.

        Returns:
        - review_chain (LLMChain): Initialized LLMChain for quiz evaluation.

        On Failure: Raises a McqGeneratorException in case of an initialization error.

        Version: 1.0
        """
        try:
            logging.info("Initializing quiz evaluation chain...")
            quiz_evaluation_prompt = PromptTemplate(input_variables=["subject", "quiz"], template=self.template2)

            review_chain = LLMChain(llm=self.llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=self.verbose)

            logging.info("Quiz evaluation chain initialized successfully.")
            return review_chain
        except Exception as e:
            raise McqGeneratorException(e, sys)

    
    def instializing_evaluate_chain(self) -> Optional[dict]:
        """
        Method Name: instializing_evaluate_chain
        Description: Initialize and execute the generate and evaluate chain.

        Returns:
        - response (dict): The response from the generate and evaluate chain.

        On Failure: Raises a McqGeneratorException in case of an initialization or execution error.

        Version: 1.0
        """
        try:
            logging.info("Initializing generate and evaluate chain...")
            quiz_chain = self.quiz_generate_chain()
            review_chain = self.quiz_evaluate_chain()

            generate_evaluate_chain = SequentialChain(
                chains=[quiz_chain, review_chain],
                input_variables=["text", "number", "subject", "tone", "response_json"],
                output_variables=["quiz", "review"], verbose=True
            )
            TEXT = read_text_from_file(file_path=DATA_FILE_PATH)
            RESPONSE_JSON1 = json.dumps(RESPONSE_JSON)

            with get_openai_callback() as cb:
                response = generate_evaluate_chain({
                    "text": TEXT,
                    "number": NUMBER,
                    "subject": SUBJECT,
                    "tone": TONE,
                    "response_json": RESPONSE_JSON1
                })

            logging.info(f"Total Tokens:{cb.total_tokens}")
            logging.info(f"Prompt Tokens:{cb.prompt_tokens}")
            logging.info(f"Completion Tokens:{cb.completion_tokens}")
            logging.info(f"Total Cost:{cb.total_cost}")

            logging.info("Generate and evaluate chain executed successfully.")

            return response
        except Exception as e:
            raise McqGeneratorException(e, sys)

    def generating_mcq(self) -> None:
        """
        Method Name: generating_mcq
        Description: Generate multiple-choice questions (MCQs) and save the data in a CSV file.

        Returns: None

        On Failure: Raises a McqGeneratorException in case of an error during MCQ generation.

        Version: 1.0
        """
        try:
            logging.info("Starting MCQ generation...")
            
            response = self.instializing_evaluate_chain()

            quiz = response.get('quiz')

            quiz = json.loads(quiz)

            # Generate a table of quiz data
            quiz_table_data = generate_quiz_table_data(quiz)

            # Write quiz data to a CSV file
            converting_data_in_csv = write_quiz_data_to_csv(quiz_table_data=quiz_table_data, csv_filename=MCQ_FILE_PATH)

            logging.info("MCQ generation completed successfully.")
            return converting_data_in_csv

        except Exception as e:
            raise McqGeneratorException(e, sys)