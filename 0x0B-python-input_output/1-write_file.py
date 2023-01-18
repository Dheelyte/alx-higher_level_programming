#!/usr/bin/python3
"""This module contains ```write_file``` function"""


def write_file(filename="", text=""):
    """"writes a string to a text file (UTF8)"""

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
