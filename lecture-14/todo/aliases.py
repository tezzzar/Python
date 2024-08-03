from typing import List, Union, TypeAlias, Dict, Any

# Список рядків
StrList: TypeAlias = List[str]

# Список списків, де кожен список містить рядки, цілі числа або None
ListUnion: TypeAlias = List[List[Union[str, int, None]]]

# Список словників, де кожен словник має рядкові ключі та значення будь-якого типу
TodoListDict: TypeAlias = List[Dict[str, Any]]

# Словник з рядковими ключами та значеннями будь-якого типу
DictStr: TypeAlias = Dict[str, Any]
