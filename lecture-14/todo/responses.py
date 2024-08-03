from typing import NamedTuple
from todo.aliases import DictStr, TodoListDict


class TodoResponse(NamedTuple):
    """
    Представляє відповідь для одного завдання.

    Атрибути:
        todo (DictStr): Словник, що містить деталі завдання.
        error (int): Код помилки, що відображає статус операції.
    """

    todo: DictStr
    error: int


class DBResponse(NamedTuple):
    """
    Представляє відповідь для операції з базою даних, що включає список завдань.

    Атрибути:
        todo_list (TodoListDict): Словник, що містить список завдань.
        error (int): Код помилки, що відображає статус операції.
    """

    todo_list: TodoListDict
    error: int
