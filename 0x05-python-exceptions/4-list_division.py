#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            div = 0
        except TypeError:
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        finally:
            new_list.append(div)
    return new_list
