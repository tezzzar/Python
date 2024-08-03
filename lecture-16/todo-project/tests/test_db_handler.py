import pytest
from unittest.mock import patch, mock_open
from todo.db_handler import DBHandler

from todo import DB_READ_ERROR, DB_WRITE_ERROR, FILE_ERROR, SUCCESS, DIR_ERROR

from pathlib import Path

test_db_path = Path.home().joinpath('.' + Path.home().stem + "_todo.json")


def test_read_todos_success(mocker):
    mocker.patch('builtins.open', mock_open(read_data='''[{
        "task": "Todo Somethig Else.",
        "category": "Work",
        "added_at": "2024-07-10T15:55:13.491836",
        "completed_at": null,
        "status": 1,
        "position": 0
    }]'''))
    db_handler = DBHandler(Path(test_db_path))
    response = db_handler.read_todos()
    assert len(response.todo_list) == 1
    assert response.todo_list[0]['task'] == "Todo Somethig Else."
    assert response.todo_list[0]['category'] == "Work"


