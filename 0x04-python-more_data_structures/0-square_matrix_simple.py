#!/usr/bin/python3


def sq(num):
    return num * num


def square_matrix_simple(matrix=[]):
    b = []
    for x in matrix:
        a = []
        for y in x:
            a.append(sq(y))
        b.append(a)
    return b
