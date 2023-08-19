import os
from  pathlib import Path
import logging

logging.basicConfig(level=logging.info, format='[%(ascitime)s]:%(message)s:')

project_name= "textSummarizer"

#CI/Cd related YAML file
list_of_files = [
    ".github/workflows/.gitkeep", # takes code from git ad deployes automatically
    f"src/{project_name}/__init_py.", #constrctor file for local package 
    f"src/{project_name}/components/__init_py.",
    f"src/{project_name}/utils/__init_py."
]