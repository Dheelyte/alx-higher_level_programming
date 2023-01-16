#!/usr/bin/python3
"""contains is_same_class"""


def is_same_class(obj, a_class):
    """True if the object is exactly an instance of the specified class"""
    return (type(obj) == a_class)
