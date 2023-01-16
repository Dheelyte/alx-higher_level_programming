#!/usr/bin/python3
"""This module contains an empty class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiate a new Rectangle"""
        self.__width = super().integer_validator("width", width)
        self.__width = width
        self.__height = super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(str(self.__width), str(self.__height)))
