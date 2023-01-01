#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    [new_list.append(item) for item in set_1 if item not in set_2]
    return new_list
