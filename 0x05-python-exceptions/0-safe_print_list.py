#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    for i in my_list[:x]:
        try:
            print(i, end="")
            length += 1
        except IndexError:
            break
    print()
    return length
