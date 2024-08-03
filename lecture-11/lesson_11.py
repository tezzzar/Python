# Завдання 1
print("Завдання 1")

import time

"""" Це функція декоратор, яка за допомогою модуля time викликає затримку на 5 сек. """


def delay(seconds):
    def decorator(func):
        def wrapped_function(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)

        return wrapped_function

    return decorator


# Застосування декоратора delay над функцією it_may_be робить її аргументом для декоратора delay
@delay(5)
def it_may_be(name=""):
    return f"{name} ask: It's nearly Luncheon Time?\n"


# Вінні-Пух запитує: "Вже майже час обіду?"
for _ in range(12):
    print(it_may_be(name="Winnie-the-Pooh"))


print()
