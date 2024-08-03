import configparser
from pathlib import Path
from typing import Any
import typer

from todo import DB_WRITE_ERROR, DIR_ERROR, FILE_ERROR, SUCCESS, __app_name__

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))

CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"


def _init_config_file() -> int:
    """
    Ініціалізує конфігураційний файл, створюючи необхідні директорії та файл.

    Спробує створити директорію для конфігураційного файлу, якщо вона не існує,
    та сам конфігураційний файл, якщо його також немає.

    Повертає:
        int: Код помилки, якщо сталася проблема (DIR_ERROR або FILE_ERROR)
        або SUCCESS, якщо все успішно.
    """
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR
    return SUCCESS


def _create_database(db_path: Any) -> int:
    """
    Створює конфігураційний файл з інформацією про базу даних.

    Створює новий конфігураційний файл або оновлює існуючий,
    додаючи в нього шлях до бази даних.

    Аргументи:
        db_path (Any): Шлях до бази даних, який потрібно зберегти у конфігураційному файлі.

    Повертає:
        int: Код помилки, якщо сталася проблема (DB_WRITE_ERROR), або SUCCESS, якщо все успішно.
    """
    config_parser = configparser.ConfigParser()
    config_parser["General"] = {"database": db_path}

    try:
        with CONFIG_FILE_PATH.open("w") as file:
            config_parser.write(file)
    except OSError:
        return DB_WRITE_ERROR
    return SUCCESS


def init_app(db_path: Any) -> int:
    """
    Ініціалізує конфігурацію додатка, створюючи конфігураційний файл і записуючи шлях до бази даних.

    Спочатку викликає _init_config_file для створення директорії і файлу конфігурації.
    Потім викликає _create_database для запису шляху до бази даних у конфігураційний файл.

    Аргументи:
        db_path (Any): Шлях до бази даних.

    Повертає:
        int: Код помилки, якщо сталася проблема на будь-якому з етапів (DIR_ERROR, FILE_ERROR, DB_WRITE_ERROR)
             або SUCCESS, якщо все успішно.
    """
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    database_code = _create_database(db_path)
    if database_code != SUCCESS:
        return database_code

    return SUCCESS
