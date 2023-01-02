#!/usr/bin/python3
def best_score(a_dictionary):
    return dict(sorted(a_dictionary.items(), key=lambda item: item[1]))
