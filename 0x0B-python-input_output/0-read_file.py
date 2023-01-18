#!/usr/bin/python3
"""contains a function ```read_file```"""


def read_file(filename=""):
    """read a text file (UTF8) and prints it to stdout"""

    with open(filename, encoding="utf-8") as f:
        [print(line, end="") for line in f.readlines()]
