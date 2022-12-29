#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 65:
            print("{}".format(chr(ord(c) - 32)))
