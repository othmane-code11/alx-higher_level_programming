#!/usr/bin/python3
def replace_in_list(my_list, x, element):
    if x < 0 or x > len(my_list) - 1:
        return my_list
    else:
        my_list[x] = element
        return my_list
