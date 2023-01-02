#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sorted_dict = dict(sorted(a_dictionary.items(), key=lambda item: item[1]))
    return list(sorted_dict)[-1]
