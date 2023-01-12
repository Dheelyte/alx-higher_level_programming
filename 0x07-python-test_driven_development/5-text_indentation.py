#!/usr/bin/python3
"""prints a text with 2 new lines after each of certain characters"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace("? ", "?").replace(". ", ".").replace(": ", ":").replace("\n ", "\n").replace(" \n", "\n").strip(" ")
    for char in text:
        if char in ".?:":
            print(char)
            print("")
        else:
            print(char, end="")
