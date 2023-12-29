# Building End-To-End MCQ Generator Application

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Conda](https://img.shields.io/badge/Conda-4.9.0-green.svg)](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
[![Visual Studio Code](https://img.shields.io/badge/VS_Code-Latest-blue.svg)](https://code.visualstudio.com/download)
[![Langchain](https://img.shields.io/badge/Langchain-Your_Link-red.svg)](your-langchain-link)
[![OpenAI](https://img.shields.io/badge/OpenAI-Latest-orange.svg)](https://beta.openai.com/signup/)


## Overview

Welcome to the End-To-End MCQ Generator Application project! This application streamlines the process of generating Multiple-Choice Questions (MCQs) for various subjects and purposes.

## Introduction

The End-To-End MCQ Generator Application simplifies the creation of high-quality MCQs through intelligent question generation and customizable templates. The application aims to enhance the question generation workflow, ensuring efficiency and adherence to educational standards.

## Features

1. **Intelligent Question Generation:**
   - Leverage natural language processing and machine learning for contextually relevant MCQs.
   
2. **Customizable Question Templates:**
   - Provide a range of templates for diverse question structures and formats.
   
3. **Integration with Language Models:**
   - Integrate with language models, such as OpenAI's GPT-3, for advanced question generation.

4. **User-Friendly Interface:**
   - Develop an intuitive and user-friendly interface for easy navigation.

5. **Export and Sharing Options:**
   - Export generated MCQs in different formats and share them seamlessly.


## The structure is organized as follows:

- `.github/workflows/`: GitHub Actions workflow configuration files.
- `src/`: Source code directory containing Python modules for the deep learning model.
- `tests/`: Unit and integration test cases and test data.
- `configs/`: Configuration files, including `config.yaml` for model hyperparameters.
- `params.yaml`: Hyperparameters and configuration.
- `init_setup.sh`: Initialization script for setting up the project.
- `requirements.txt`: Python package dependencies.
- `setup.py`: Python package setup script.
- `setup.cfg`: Configuration for package distribution.
- `pyproject.toml`: Project metadata.
- `tox.ini`: Configuration for testing environments.
- `research/`: Research-related files, including a Jupyter Notebook for experiments (`trials.ipynb`).
- `.env` : All Secreat variables avilable here.

## Prerequisites

1. **Environment Variables (.env file):**
   - Create an `.env` file with the following content:
     ```dotenv
     OPENAI_API_KEY=your_api_key_here
     ```

2. **Conda:**
   - Make sure Conda is installed on your system. If not, you can install it by [following the official Conda installation guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

3. **IDE (Choose one):**
   - [Visual Studio Code](https://code.visualstudio.com/download)
   - [PyCharm](https://www.jetbrains.com/pycharm/download/)

4. **OPENAI API Key:**
   - Obtain an API key from OpenAI. You can sign up for an account and get your API key [here](https://beta.openai.com/signup/).

## Modification

In the `.env` file, replace `your_api_key_here` with your actual OpenAI API key.


## Getting Started

Follow the steps outlined in the [Installation](#installation) section to set up [Building End-To-End MCQ Generator Application] on your local machine.

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/SuyodhanJ6/End-To-End-Quiz-Generator.git

2. Create ./venv 
   ```shell 
   conda create -p ./venv python=3.8 -y

3. Activate ./venv 
   ```shell 
   conda activate ./venv

4. Run the script:
   ```shell
   stramlit run app.py

- The script will be run the application.

## License
- This script is open-source and available under the MIT License. You are free to use and modify it for your projects.

## Contribution
- Contributions are welcome! If you have ideas for improvements or new features, please open an issue or submit a pull request.

## Contact
- For questions or feedback, feel free to reach out to the project maintainers at prashantmalge181@gmail.com or create an issue on GitHub.

Enjoy streamlining your project setup process with the Project Template Generator Script!