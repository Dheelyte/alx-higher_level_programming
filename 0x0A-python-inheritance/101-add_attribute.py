#!/usr/bin/python3
"""Contains add_attribute function"""


def add_attribute(obj, attr, value):
    """add a new attribute to class

    Args:
        obj: object to add attribute to.
        attr: Attribute to be added.
        value: value of attribute to be added.

    Returns:
        TypeError if object already has an attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
