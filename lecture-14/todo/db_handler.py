"""This module provides the To-Do database functionality."""

import logging
from pathlib import Path
import json

from todo import DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR, SUCCESS
from todo.responses import DBResponse
from todo.aliases import TodoListDict


class DBHandler:
    """Handles database operations for To-Do tasks."""

    def __init__(self, db_path: Path) -> None:
        """Initialize the DBHandler with the path to the database."""
        self._db_path = db_path
        self.logger = logging.getLogger(__name__)

        self.logger.setLevel(logging.INFO)

        self.stream_handler = logging.StreamHandler()
        self.database_handler = logging.FileHandler("database_logging.log")

        self.stream_handler.setLevel(logging.WARNING)
        self.database_handler.setLevel(logging.INFO)

        # Create formatters and add them to handlers
        self.stream_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
        self.database_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        self.stream_handler.setFormatter(self.stream_format)
        self.database_handler.setFormatter(self.database_format)

        self.logger.addHandler(self.stream_handler)
        self.logger.addHandler(self.database_handler)

    def write_todos(self, todo_list: TodoListDict) -> DBResponse:
        """Write the todo list to the database file."""
        try:
            with self._db_path.open("w") as db:
                json.dump(todo_list, db, indent=4)
            return DBResponse(todo_list, SUCCESS)

        except OSError:  # Catch file IO problems
            self.logger.exception("Exception occurred while writing to the database")
            return DBResponse(todo_list, DB_WRITE_ERROR)

    def read_todos(self) -> DBResponse:
        """Read the todo list from the database file."""
        try:
            with self._db_path.open("r") as db:
                try:
                    self.logger.warning(
                        "Opened database %s for tasks reading", self._db_path
                    )
                    self.logger.info("Database was read successfully!")

                    return DBResponse(json.load(db), SUCCESS)
                except json.JSONDecodeError:  # Catch wrong JSON format
                    self.logger.exception("Exception occurred due to JSON format error")
                    return DBResponse([], JSON_ERROR)
        except OSError:  # Catch file IO problems
            self.logger.exception("Exception occurred while reading from the database")
            return DBResponse([], DB_READ_ERROR)
