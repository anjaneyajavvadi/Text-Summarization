import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    """
    Reads a YAML file and converts it into a ConfigBox."""
    try:
        with open(path_to_yaml, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"YAML file:{path_to_yaml} loaded successfully")
        return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directory(path_to_directories:list,verbose=True):
    """
    Creates directories specified in the list.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if(verbose):
            logger.info(f"Created directory: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"