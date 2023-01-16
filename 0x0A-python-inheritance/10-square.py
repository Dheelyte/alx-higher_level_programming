#!/usr/bin/python3
"""Square that inherits from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square class"""
    def __init__(self, size):
        """Initialise a new square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size 
