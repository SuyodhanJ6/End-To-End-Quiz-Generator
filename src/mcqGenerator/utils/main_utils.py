import os, sys
import pandas as pd
import yaml

from mcqGenerator.logger import logging
from mcqGenerator.exception import McqGeneratorException

def generate_quiz_table_data(quiz) -> list:
    """
    Method Name: generate_quiz_table_data
    Description: Generate a table of quiz data for display.

    Input:
    - quiz (dict): A dictionary containing quiz data.(json)

    Output:
    - quiz_table_data (list): A list of dictionaries representing quiz data in tabular format.

    On Failure: Raises an exception if the input is not in the expected format.

    Version: 1.0
    """
    try:
        quiz_table_data = []
        for key, value in quiz.items():
            mcq = value["mcq"]
            options = " | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value["options"].items()
                ]
            )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
        return quiz_table_data

    except Exception as e:
        raise McqGeneratorException(e, sys)
    

def read_text_from_file(file_path):
    """
    Method Name: read_text_from_file
    Description: Read the contents of a file and return the text.
    
    Input:
    - file_path (str): The path to the file to be read.

    Output:
    - text (str): The contents of the file as a string.

    On Failure: Raises an exception if the file cannot be read or does not exist.
    
    Version: 1.0
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except Exception as e:
        raise McqGeneratorException(e, sys)
    

def write_quiz_data_to_csv(quiz_table_data, csv_filename):
    """
    Method Name: write_quiz_data_to_csv
    Description: Write quiz data to a CSV file.

    Input:
    - quiz_table_data (list): A list of dictionaries containing quiz data.
    - csv_filename (str): The desired filename for the CSV file.

    Output: None

    On Failure: Raises an exception if there are issues during the CSV writing process.

    Version: 1.0
    """
    try:
        # Convert the list of dictionaries to a DataFrame
        quiz_df = pd.DataFrame(quiz_table_data)

        # Write the DataFrame to a CSV file
        quiz_df.to_csv(csv_filename, index=False)

        logging.info(f"Quiz data has been successfully written to {csv_filename}")
    except Exception as e:
        raise McqGeneratorException(e, sys)


def load_llm_config(file_path):
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    return config.get("llm_config", {})