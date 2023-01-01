#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        sum_2 = 0 + tuple_b[1]
    if len(tuple_b) < 2:
        sum_2 = tuple_a[1] + 0
    if len(tuple_a) >= 2 and len(tuple_b) >= 2: 
        sum_2 = tuple_a[1] + tuple_b[1]
    sum_1 = tuple_a[0] + tuple_b[0]
    return (sum_1, sum_2)
