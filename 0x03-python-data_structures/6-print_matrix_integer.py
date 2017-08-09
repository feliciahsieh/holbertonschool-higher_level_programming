#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
#    if len(matrix) == 0 or len(matrix) == 1:
#        print()
#        return
    if matrix is None or matrix == "":
       print()
    for row in matrix:
        for count, elem in enumerate(row):
            if count < len(row):
                print('{:d}'.format(elem), end="")
            else:
                print('{:d}'.format(elem), end=" ")
        print()
