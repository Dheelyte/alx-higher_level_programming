#!/usr/bin/python3
"""This module prints a square with the character #"""


def print_square(size=0):
    """a function that prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for col in range(size):
            for row in range(size):
                print("#", end="")
            print("")
