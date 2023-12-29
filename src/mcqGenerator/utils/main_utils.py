import yaml
from src.exception import MoneyLaunderingException
from src.deepClassifier.logger import logging
from src.logger import logging
import os,sys
import numpy as np
import dill

def read_yaml_file(file_path: str) -> dict:
    """
    Method Name: read_yaml_file
    Description: Reads a YAML file and returns its content as a dictionary.
    
    Input:
    - file_path (str): Path to the YAML file.
    
    Output: Dictionary containing the content of the YAML file.
    
    On Failure: Raises an exception with error details.
    
    Version: 1.0
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        # If an exception occurs, raise it with error details
        raise MoneyLaunderingException(e, sys) from e



def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Method Name: write_yaml_file
    Description: Writes content to a YAML file.
    
    Input:
    - file_path (str): Path to the YAML file.
    - content (object): Content to be written to the YAML file.
    - replace (bool): If True, replace the existing file; if False, append to it. Default is False.
    
    Output: None
    
    On Failure: Raises an exception with error details.
    
    Version: 1.0
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        # If an exception occurs, raise it with error details
        raise MoneyLaunderingException(e, sys)




def save_numpy_array_data(file_path: str, array: np.array):
    """
    Method Name: save_numpy_array_data
    Description: Save numpy array data to a binary file.
    
    Input:
    - file_path (str): Location of the file to save.
    - array (np.array): Numpy array data to save.
    
    Output: None
    
    On Failure: Raises an exception with error details.
    
    Version: 1.0
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        # If an exception occurs, raise it with error details
        raise MoneyLaunderingException(e, sys) from e



def load_numpy_array_data(file_path: str) -> np.array:
    """
    Method Name: load_numpy_array_data
    Description: Load numpy array data from a binary file.
    
    Input:
    - file_path (str): Location of the file to load.
    
    Output: np.array data loaded from the file.
    
    On Failure: Raises an exception with error details.
    
    Version: 1.0
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        # If an exception occurs, raise it with error details
        raise MoneyLaunderingException(e, sys) from e



def save_object(file_path: str, obj: object) -> None:
    """
    Method Name: save_object
    Description: Save an object to a binary file using dill library.
    
    Input:
    - file_path (str): Location of the file to save.
    - obj (object): Object to be saved.
    
    Output: None
    
    On Failure: Raises an exception with error details.
    
    Version: 1.0
    """
    try:
        logging.info("Entered the save_object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of MainUtils class")
    except Exception as e:
        # If an exception occurs, raise it with error details
        raise MoneyLaunderingException(e, sys) from e



def load_object(file_path: str) -> object:
    """
    Method Name: load_object
    Description: Load an object from a binary file using dill library.
    
    Input:
    - file_path (str): Location of the file to load.
    
    Output: The loaded object.
    
    On Failure: Raises an exception if the file doesn't exist or if there's an error during loading.
    
    Version: 1.0
    """
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file: {file_path} does not exist")
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        # If an exception occurs, raise it with error details
        raise MoneyLaunderingException(e, sys) from e


