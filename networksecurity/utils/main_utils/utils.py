import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import os, sys  
import numpy as np 
import pandas as pd   
import dill  
import pickle


def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    # end try
    
def write_yaml_file(file_path: str, content: dict, replace: bool = False):
    try:
        # Always create the directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        if replace and os.path.exists(file_path):
            os.remove(file_path)
            
        with open(file_path, "w") as file:
            yaml.dump(content, file, default_flow_style=False)  
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    