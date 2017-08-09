#!/usr/bin/python3


def _add(a, b):
    return (a + b)


def add_tuple(tuple_a=(), tuple_b=()):
    new = [0, 0]
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = tuple_a + (0,)

    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = tuple_b + (0,)

    for i in range(2):
        new[i] = tuple_a[i] + tuple_b[i]

    return tuple(new)
