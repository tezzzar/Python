class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


import pytest


class TestGetAreaRectangle:
    def test_normal_case(self):
        rect = Rectangle(2, 3)
        assert rect.get_area() == 6, "incorrect area"

    def test_negative_case(self):
        rect = Rectangle(-1, 2)
        assert rect.get_area() == -1, "incorrect negative output"
