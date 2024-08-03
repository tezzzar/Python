def add(x, y):
    """Функція для додавання двох чисел"""
    return x + y


def subtract(x, y):
    """Функція для віднімання одного числа від іншого"""
    return x - y


def multiply(x, y):
    """Функція для множення двох чисел"""
    return x * y


def divide(x, y):
    """Функція для ділення одного числа на інше"""
    if y == 0:
        return None, "Ой, ділення на нуль"
    return x / y, ""


def modulo(x, y):
    """Функція для знаходження остачі від ділення"""
    if y == 0:
        return None, "Ой, ділення на нуль"
    return x % y, ""


def idivide(x, y):
    """Функція для цілої частини від ділення одного числа на інше"""
    if y == 0:
        return None, "Ой, ділення на нуль"
    return x // y, ""


def exponent(x, y):
    """Функція для підняття числа x в ступінь y"""
    return x**y


def calc_help(e=""):
    if e:
        print(f"\n{e}")
    print(
        """
        Usage operation:
            h                        Display this usage message
            2 + 2                    Add
            3 - 1                    Subtract
            2 * 2                    Multiply
            4 / 2                    Divide
            5 // 2                   Int Divide
            7 % 3                    Modulo Divide
            2 ** 3                   Exponentiation
            q                        Quit
        """
    )
