#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    common = []
    for x in set_1:
        if x in set_2:
            common.append(x)

    list = []
    for y in set_1 | set_2:
        if y not in common:
            list.append(y)
    return list
