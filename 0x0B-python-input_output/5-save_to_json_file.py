#!/usr/bin/python3
"""This module contains ```save_to_json_file``` function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON rep."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
