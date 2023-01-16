#!/usr/bin/python3
"""This module contains an empty class BaseGeometry"""


class BaseGeometry:
    """A Geometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiate a new Rectangle"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
