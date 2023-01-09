#!/usr/bin/python3

"""Write a class Square that defines a square by."""


class Square():

    """A class Square that defines a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.area()

    @property
    def size(self):
        """Setter method that returns the size of a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method that sets the size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of a square."""
        return self.__size**2

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
