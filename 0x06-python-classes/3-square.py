#!/usr/bin/python3

"""Write a class Square that defines a square by."""


class Square():

    """A class Square that defines a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of a square."""
        return self.__size**2
