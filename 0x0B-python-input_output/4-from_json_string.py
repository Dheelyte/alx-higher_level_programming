#!/usr/bin/python3
import json
"""This module contains from_json_string function"""


def from_json_string(my_str):

    """returns an object represented by a JSON string"""
    return json.loads(my_str)
