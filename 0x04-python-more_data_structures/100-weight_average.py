#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_fx = 0
    sum_f = 0
    for i in my_list:
        sum_fx += i[0] * i[1]
        sum_f += i[1]
    return sum_fx/sum_f
