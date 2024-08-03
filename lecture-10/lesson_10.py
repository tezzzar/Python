# Завдання 1
print("Завдання 1")

import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.set_r(r)

    def length(self):
        """Повертає довжину кола."""
        return 2 * math.pi * self.r

    def square(self):
        """Повертає площу кола."""
        return math.pi * self.r**2

    def set_r(self, r):
        """Встановлює радіус кола."""
        assert r > 0, "Радіус має бути позитивним числом!"
        self.r = r


c = Circle(3, 4, 1)
print(c.length(), c.square())

try:
    c.set_r(-1)
except AssertionError as e:
    print(e)

print()
