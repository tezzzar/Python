"""This module provides helper functions for the To-Do application."""

from typing import Any
import typer
from rich.prompt import Prompt
from rich import print as rprint

from todo import __app_name__, __version__
from todo.model import Todo


def make_title(fn: Any) -> Any:
    """Decorator to format the title of a function's output."""

    def wrapper() -> Any:
        func = fn()
        output = func.title()
        return output

    return wrapper


@make_title
def add_your_task() -> str:
    """Prompt user to input a task."""
    return Prompt.ask(
        "[bold green on blue] Text Your task [/]", default="Todo something else"
    )


def join_category() -> str:
    """Return a string representation of available categories."""
    res = ""
    for category, color in Todo.COLORS.items():
        res += f"[bold white on {color}] {category} [/]"
    return res


@make_title
def choose_category() -> str:
    """Prompt user to choose a category."""
    return Prompt.ask(
        "[bold green on blue] Choose category [/]" + join_category(), default="Work"
    )


def hello() -> None:
    """Print a welcome message with application name and version."""
    rprint(
        f"[bold magenta]{__app_name__.upper()}[/bold magenta]",
        chr(128187),
        f"[bold magenta]{__version__}[/bold magenta]",
    )


def make_your_choice() -> str:
    """Prompt user to make a choice."""
    return Prompt.ask("[bold green on blue] Make Your Choice (a|l|u|r|q) [/]")


def bye(title: str) -> None:
    """Print a goodbye message."""
    typer.secho(
        f"Thanks for using {title}. Have a nice day!", fg=typer.colors.BRIGHT_GREEN
    )


def help_me() -> None:
    """Print the help message."""
    typer.secho(
        """
    All that You can do:
        l : List existing tasks
        a : Add new task
        u : Update existing task
        r : Remove existing task
        h : Print this help
        q : Exit
    """,
        fg=typer.colors.BRIGHT_GREEN,
        bg=typer.colors.BRIGHT_WHITE,
    )


def choice_id() -> int:
    """Dummy function to return an ID. Replace with actual implementation."""
    return 1
