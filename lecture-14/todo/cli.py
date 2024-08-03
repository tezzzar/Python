"""CLI для управління завданнями."""

import logging
from pathlib import Path
from typing import Any
import typer
from rich.console import Console
from rich.table import Table

from todo import __app_name__, __version__, TITLE, ERRORS
from todo.helpers import Any
from todo.helpers import (
    add_your_task,
    hello,
    make_your_choice,
    bye,
    help_me,
    choose_category,
)
from todo.model import Todo
from todo.todos import TodoList
from todo import db, config, todos

app = typer.Typer()
console = Console()
header = Todo.make_header()

# Налаштування логування
import logging

# Налаштування основного конфігуратора для файлу
logging.basicConfig(
    filename="todo.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Додавання обробника для консолі
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)

# Отримання кореневого логера та додавання обробника
logger = logging.getLogger()
logger.addHandler(console_handler)


def show(tasks: Any) -> None:
    """Відобразити список завдань у таблиці."""
    table = Table(show_header=True, header_style="bold blue")
    for item in header:
        table.add_column(
            item["name"],
            style=item["style"],
            width=item["width"],
            min_width=item["min_width"],
            justify=item["justify"],
        )

    for index, task in enumerate(tasks, start=1):
        c = Todo.get_category_color(task["category"])
        is_done = Todo.DONE if task["status"] == 2 else Todo.PENDING
        table.add_row(
            str(index), task["task"], f'[{c}]{task["category"]}[/{c}]', is_done
        )

    console.print(table)


def get_todo_list() -> todos.TodoList:
    """Отримати список завдань з бази даних."""
    if config.CONFIG_FILE_PATH.exists():
        db_path = db.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho(
            'Config file not found. Please, run "todo init"', fg=typer.colors.RED
        )
        logging.error("Config file not found.")
        raise typer.Exit(1)

    if db_path.exists():
        return todos.TodoList(db_path)

    typer.secho('Database not found. Please, run "todo init"', fg=typer.colors.RED)
    logging.error("Database not found.")
    raise typer.Exit(1)


@app.command()
def init(
    db_path: str = typer.Option(
        str(db.DEFAULT_DB_FILE_PATH),
        "--db-path",
        "-db",
        prompt="to-do database location?",
    )
) -> None:
    """Ініціалізувати конфігураційний файл та базу даних."""
    app_init_error = config.init_app(db_path)
    if app_init_error:
        typer.secho(
            f"Creating config file failed with {ERRORS[app_init_error]}",
            fg=typer.colors.RED,
        )
        logging.error("Creating config file failed with %s", ERRORS[app_init_error])
        raise typer.Exit(1)

    db_init_error = db.init_database(Path(db_path))
    if db_init_error:
        typer.secho(
            f"Creating database failed with {ERRORS[db_init_error]}",
            fg=typer.colors.RED,
        )
        logging.error("Creating database failed with %s", ERRORS[db_init_error])
        raise typer.Exit(1)

    typer.secho(f"The todo database is {db_path}", fg=typer.colors.GREEN)
    logging.info("The todo database is %s", db_path)


@app.command()
def run() -> None:
    """Основна функція для запуску додатку."""
    hello()
    todo_list = get_todo_list()

    while True:
        choice = make_your_choice()
        if choice == "a":
            category = choose_category()
            task = add_your_task()
            current_todo, write_error = todo_list.add(task, category)

            if write_error:
                typer.secho(
                    f"Adding task failed with {write_error}", fg=typer.colors.RED
                )
                logging.error("Adding task %s failed with %s", task, write_error)
                raise typer.Exit(1)

            typer.secho(
                f"Task {task} was added to todo database with {category}",
                fg=typer.colors.GREEN,
            )
            logging.info("Task %s was added to todo database with %s", task, category)

        elif choice == "l":
            tasks, error = todo_list.get_todo()
            if error:
                typer.secho(
                    f"Fetching tasks failed with {ERRORS[error]}",
                    fg=typer.colors.RED,
                )
                logging.error("Fetching tasks failed with %s", ERRORS[error])
                raise typer.Exit(1)

            if len(tasks) == 0:
                typer.secho(
                    "There are no tasks in the to-do list yet",
                    fg=typer.colors.RED,
                )
                logging.info("No tasks in the to-do list")
                raise typer.Exit()

            show(tasks)
            logging.info("Displayed tasks successfully")

        elif choice == "u":
            task_id = helpers.choose_id()
            tasks, error = todo_list.complete(task_id)
            if error:
                typer.secho(
                    f"Completing task failed with {ERRORS[error]}",
                    fg=typer.colors.RED,
                )
                logging.error(
                    "Completing task with id %d failed with %s", task_id, ERRORS[error]
                )
                raise typer.Exit(1)

            show(tasks)
            logging.info("Task with id %d completed", task_id)

        elif choice == "r":
            task_id = helpers.choose_id()
            tasks, error = todo_list.delete(task_id)
            if error:
                typer.secho(
                    f"Deleting task failed with {ERRORS[error]}",
                    fg=typer.colors.RED,
                )
                logging.error(
                    "Deleting task with id %d failed with %s", task_id, ERRORS[error]
                )
                raise typer.Exit(1)

            show(tasks)
            logging.info("Task with id %d deleted", task_id)

        elif choice == "q":
            bye(TITLE)
            logging.info("User exited the application")
            break

        else:
            help_me()
            logging.warning("Unknown command entered")
