#!/usr/bin/python3
def new_in_list(my_list, x, element):
    copy = my_list.copy()
    if x < 0 or x > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[x] = element
        return copy
