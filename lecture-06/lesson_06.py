from calculator import *
from operations import *

title = "Super Calc"


def menu():
    """Функція для виведення меню калькулятора"""
    print(f"{title}".title().center(40, "="), "\n")
    print("_" * 40)
    str1 = "Вибір операції:"
    print("|" + str1 + " " * (38 - len(str1)) + "|")
    print("|" + "_" * 38 + "|")
    print("| c : Обчислити".ljust(39, " ") + "|")
    print("| h : Допомога".ljust(39, " ") + "|")
    print("| q : Вихід".ljust(39, " ") + "|")
    print("=" * 40)

    choice = input("| Введіть вибір (h|c|q): ".title()).lower()
    return choice if choice in ("h", "c", "q") else "h"


while True:
    choice = menu()

    if choice == "q":
        print("Дякуємо, що користувалися Super Calc!")
        break

    if choice == "h":
        calc_help()
        continue

    if choice == "c":
        entry = input("Введіть x оператор y (наприклад, 2 + 2): ")
        a, b, operator = extract(entry)

        if not operator:
            calc_help("Некоректний формат або недопустимий оператор.")
            continue

        res, err = result(a, b, operator)
        if err:
            print(err)
        else:
            print(f"{a} {operator} {b} = {res}")
