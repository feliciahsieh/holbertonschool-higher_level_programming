#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if 0 <= idx < (len(my_list)):
        a = []
        a.append(element)
        my_list = my_list[:idx] + a + my_list[idx + 1:]
        return my_list
    else:
        return my_list
