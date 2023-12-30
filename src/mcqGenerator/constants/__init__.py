from pathlib import Path

"""
MCQ 
"""
PIPELINE_NAME:str = 'mcq'
ARTIFACT_DIR: str = "artifact"


DATA_FILE_PATH = Path("/home/suyodhan/Documents/Generative-AI-Project/End-To-End-Quiz-Generator/dataset/data.txt")

MCQ_GENERATOR_DIR: str = "mcq_generator"
# Tokens
NUMBER: int =5 
SUBJECT: str="data sciecne"
TONE: str ="simple"

## PARAMETER RELEATED CONSTANT
PARMS_FILE_PATH = Path("/home/suyodhan/Documents/Generative-AI-Project/End-To-End-Quiz-Generator/params.yaml")

## OUTPUT CSV FILE NAME (MCQ_FILE_PATH)
MCQ_FILE_PATH = Path("/home/suyodhan/Documents/Generative-AI-Project/End-To-End-Quiz-Generator/dataset/output_mcq.csv")