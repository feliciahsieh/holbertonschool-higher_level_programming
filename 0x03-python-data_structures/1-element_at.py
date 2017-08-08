#!/usr/bin/python3


def element_at(my_list, idx):
    if type(idx) is str:
        return None
    elif idx >= len(my_list):
        return None
    elif idx < 0 and abs(idx) > len(my_list):
        return None
    else:
        return my_list[idx]
