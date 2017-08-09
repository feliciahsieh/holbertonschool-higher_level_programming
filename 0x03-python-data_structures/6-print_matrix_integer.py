#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        if len(element) == 1 or len(element) == 0:
            print()
        print(" ".join("{}".format(i) for i in element))
