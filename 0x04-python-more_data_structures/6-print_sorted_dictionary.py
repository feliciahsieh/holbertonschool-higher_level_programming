#!/usr/bin/python3


def print_sorted_dictionary(my_dict):
    a = sorted(my_dict)
    for i in a:
        print('{}: {}'.format(i, my_dict[i]))
