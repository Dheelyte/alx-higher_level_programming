#!/usr/bin/python3
"""Contains is_kind_of_class class"""


def is_kind_of_class(obj, a_class):
    """Is instance of or subclass of"""
    return (isinstance(obj, a_class) or issubclass(obj, a_class))
