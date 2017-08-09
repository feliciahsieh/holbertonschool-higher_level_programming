#!/usr/bin/python3



def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 or len(matrix) == 0:
        print()
    for element in matrix:
        print(" ".join("{}".format(i) for i in element))
