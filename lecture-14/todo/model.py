"""Модель завдання"""

import datetime
from typing import Any

from todo.aliases import StrList, ListUnion, DictStr, TodoListDict


class Todo:
    """
    Представляє завдання у списку завдань.

    Атрибути класу:
        DONE (str): Символ для позначення завершеного завдання.
        PENDING (str): Символ для позначення незавершеного завдання.
        COLORS (DictStr): Словник кольорів для категорій завдань.
        keys (StrList): Список ключів для заголовків таблиці.
        values (ListUnion): Список значень для заголовків таблиці.
    """

    DONE: str = chr(9989)
    PENDING: str = chr(10060)

    COLORS: DictStr = {
        "Learn": "yellow",
        "Work": "red",
        "Sports": "cyan",
        "Study": "green",
    }

    keys: StrList = ["name", "style", "width", "min_width", "justify"]

    values: ListUnion = [
        ["#", "dim", 6, None, "left"],
        ["Todo", None, None, 20, "left"],
        ["Category", None, None, 12, "right"],
        ["Done", None, None, 12, "right"],
    ]

    @staticmethod
    def make_header() -> TodoListDict:
        """
        Створює заголовки для таблиці завдань на основі значень і ключів класу.

        Повертає:
            TodoListDict: Список словників, що представляють заголовки таблиці.
        """
        headers = []
        for v in Todo.values:
            d = dict(zip(Todo.keys, v))
            headers.append(d)
        return headers

    @staticmethod
    def get_category_color(category: str) -> Any:
        """
        Отримує колір для вказаної категорії завдання.

        Аргументи:
            category (str): Назва категорії.

        Повертає:
            Any: Колір категорії, якщо він існує, інакше "white".
        """
        if category in Todo.COLORS:
            return Todo.COLORS[category]
        return "white"

    @classmethod
    def endwith_sentence(cls, task: str) -> str:
        """
        Додає крапку в кінець завдання, якщо її немає.

        Аргументи:
            task (str): Текст завдання.

        Повертає:
            str: Текст завдання з крапкою в кінці (якщо її не було).
        """
        if not task.endswith("."):
            task += "."
        return task

    def __init__(
        self,
        task: str,
        category: str,
        added_at: Any | None = None,
        completed_at: Any | None = None,
        status: int | None = None,
        position: int | None = None,
    ) -> None:
        """
        Ініціалізує об'єкт завдання.

        Аргументи:
            task (str): Текст завдання.
            category (str): Категорія завдання.
            added_at (Any | None): Дата і час додавання завдання.
            completed_at (Any | None): Дата і час завершення завдання.
            status (int | None): Статус завдання (1 - відкрито, 2 - завершено).
            position (int | None): Позиція завдання у списку.
        """
        self._task = Todo.endwith_sentence(task)
        self._category = category
        self._added_at = (
            added_at if added_at is not None else datetime.datetime.now().isoformat()
        )
        self._completed_at = completed_at if completed_at is not NameError else None
        self._status = status if status is not None else 1  # 1 - open
        self._position = position if position is not None else None

    def to_dict(self) -> Any:
        """
        Перетворює об'єкт завдання на словник.

        Повертає:
            Any: Словник, що представляє завдання.
        """
        return {
            "task": self._task,
            "category": self._category,
            "added_at": self._added_at,
            "completed_at": self._completed_at,
            "status": self._status,
            "position": self._position,
        }

    def __repr__(self) -> str:
        """
        Повертає рядкове представлення об'єкта завдання.

        Повертає:
            str: Рядкове представлення завдання.
        """
        return str(self.to_dict())
