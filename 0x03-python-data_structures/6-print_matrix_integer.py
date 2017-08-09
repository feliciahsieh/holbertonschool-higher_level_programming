#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or len(matrix) == 1:
        print()
    for row in matrix:
        if len(row) == 0:
            print("")
            continue
        print(" ".join("{}".format(i) for i in row))
