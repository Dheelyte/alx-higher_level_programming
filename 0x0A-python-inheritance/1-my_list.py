#!/usr/bin/python3
"""Contains class MyList that inherits from list"""


class MyList(list):
    """A subclass of list"""

    def __init__(self):
        """Initialises the list subclass"""
        super().__init__()

    def print_sorted(self):
        """Printes sorted list"""
        print(sorted(self))
