#!/usr/bin/python3
"""Defines a class Student that defines a student"""


class Student():
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialization method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""

        return self.__dict__
