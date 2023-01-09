#!/usr/bin/python3

"""Write a class Square that defines a square by."""


class Square():

    """A class Square that defines a square."""

    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        self.__size = __size
