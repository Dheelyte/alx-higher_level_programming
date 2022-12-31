#!/usr/bin/python3

def remove_char_at(str, n):
    for c in str:
        if str.index(c) != n:
            print(c, end ="")
    print("")
