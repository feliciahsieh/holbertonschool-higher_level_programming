#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
#    if len(matrix) == 1 or len(matrix) == 0:
#        print()
    for element in matrix:
        print(" ".join("{}".format(i) for i in element))

"""
    i = 0
    for row in matrix:
        i = 0
        for col in row:
            if i == (len(row) - 1):
                print('{:d}'.format(col))
            else:
                print('{:d}'.format(col), end=" ")
            i = i + 1
"""
