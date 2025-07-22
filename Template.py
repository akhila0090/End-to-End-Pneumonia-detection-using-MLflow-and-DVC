import os
from pathlib import Path
import logging

# Setting  up logging format
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "PneumoniaDetector"

# Defining the project structure
file_structure = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

def create_project_structure(files: list):
    for file in files:
        file_path = Path(file)
        dir_path = file_path.parent

        # creating directories if it doesn't exist
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {dir_path}")

        # Creating the file if it doesn't exist or is empty
        if not file_path.exists() or file_path.stat().st_size == 0:
            file_path.touch()
            logging.info(f"Created empty file: {file_path}")
        else:
            logging.info(f"File already exists: {file_path}")

create_project_structure(file_structure)
