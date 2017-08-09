#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for sub_list in matrix:
        if len(sub_list) == 0:
            print("")
            continue
        print(" ".join("{}".format(i) for i in sub_list))
