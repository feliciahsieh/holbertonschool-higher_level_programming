#!/usr/bin/python3


def uniq_add(my_list=[]):
    sum = 0
    myset = set(my_list)
    for x in myset:
        sum += x
    return sum
