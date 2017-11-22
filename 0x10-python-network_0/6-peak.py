#!/usr/bin/python3
""" Find highest integer in list_of_integers """


def find_peak(list_of_integers):
    if list_of_integers is None:
        return float('-inf')
    if len(list_of_integers) == 1):
        return list_of_integers[0]
    max = list_of_integers[0]
    if max > list_of_integers[1]:
        return max
    for k, v in list_of_integers[1:-2]:
        if max < v:
            max = i
        if max > list_of_integers[k + 1]:
            return max
    return max
