#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print("")
            continue
        print(" ".join("{}".format(i) for i in row))
