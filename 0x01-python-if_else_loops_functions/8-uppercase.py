#!/usr/bin/python3
def uppercase(str):
    return "".join([chr(ord(c) - 32) for c in str if ord(c) >= 65])
