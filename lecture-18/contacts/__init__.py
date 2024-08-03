import os.path
from pathlib import Path

def init_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

__app_name__ = "contacts"
__version__ = "0.1.0"

TITLE = "Your contact book"

DATABASE_PATH = str(Path.home())  + f"/.config/{__app_name__}"
# print(DATABASE_PATH)
init_dir(DATABASE_PATH)
DATABASE = f"{DATABASE_PATH}/{__app_name__}.pkl"
