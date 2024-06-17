from operations import add, subtract, multiply, divide, modulo, idivide, exponent


ops = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "//": idivide,
    "%": modulo,
    "**": exponent,
}


def extract(entry):
    """Функція для витягування операндів і оператора з рядка введення"""
    for o in ops.keys():
        if o in entry:
            parts = entry.split(o)
            if len(parts) == 2:
                a, b = parts
                return a.strip(), b.strip(), o
    return None, None, None


def result(a, b, operator):
    """Функція для виконання обраної математичної операції"""
    try:
        a, b = float(a), float(b)
        if operator == "/" and b == 0:
            return None, "Ой, ділення на нуль"
        elif operator in ("//", "%") and b == 0:
            return None, "Ой, ділення або знаходження остачі на нуль"
        else:
            return ops[operator](a, b), ""
    except ValueError:
        return None, "Некоректний ввід. Будь ласка, введіть числові значення."
