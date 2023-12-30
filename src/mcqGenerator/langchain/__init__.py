from langchain.llms import OpenAI

from mcqGenerator.constants.env_vairable import KEY
from mcqGenerator.constants import PARMS_FILE_PATH
from mcqGenerator.utils.main_utils import load_llm_config

from mcqGenerator.logger import logging

llm_confgs = load_llm_config(file_path=PARMS_FILE_PATH)

model_name = llm_confgs.get('model_name')
logging.info(f"Model Name of LLM {model_name}")
temperature = llm_confgs.get('temperature')
logging.info(f"Temperature of LLM {temperature}")

logging.info("We Are Instializing the Object of OpenAI")
llm = OpenAI(openai_api_key=KEY, model_name=model_name, temperature=temperature)
logging.info("We are succesfully building the object of OpenAI")