#!/usr/bin/python3
roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
# LXIV
# LIVX
# LVIV
# XXX

def roman_to_int(roman_string):
    result = 0
    for value in roman_string[::-1]:
        if roman_numerals[value] >= result:
            result += roman_numerals[value]
        if roman_numerals[value] < result:
            result -= roman_numerals[value]
    return result, roman_string[::-1]
from sys import argv
print(roman_to_int(argv[1]))
