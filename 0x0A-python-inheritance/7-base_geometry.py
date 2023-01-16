#!/usr/bin/python3
"""This module contains an empty class BaseGeometry"""


class BaseGeometry():
    """A Geometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
