#!/usr/bin/python3
"""This module contains from_json_string function"""
import json


def from_json_string(my_str):

    """returns an object represented by a JSON string"""
    return json.loads(my_str)
