#!/usr/bin/python3


def search_replace(my_list, search, replace):
    a = []
    for x in my_list:
        a.append(x if x != search else replace)

    return a
