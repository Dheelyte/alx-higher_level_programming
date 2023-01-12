#!/usr/bin/python3
"""This module contains a class Rectangle that defines a rectangle"""


class Rectangle():
    """This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for height in range(self.__height):
            for width in range(self.__width):
                rect.append("#")
            if height != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    @property
    def width(self):
        """property def width(self): to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter def width(self, value): to set it"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property def height(self): to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter def height(self, value): to set it"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))
