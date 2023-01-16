#!/usr/bin/python3
"""This module contains an empty class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiate a new Rectangle"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
