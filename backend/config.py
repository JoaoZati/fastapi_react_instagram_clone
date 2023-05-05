import os

# Get the absolute path to the current directory and append the path to the backend folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(BASE_DIR, "backend") if os.path.isdir("backend") else BASE_DIR
