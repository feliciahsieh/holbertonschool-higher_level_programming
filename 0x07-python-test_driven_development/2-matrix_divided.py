#!/usr/bin/python3
"""
    Divides each element of a matrix by a divisor
"""


def matrix_divided(matrix, div):
    """
    Divides elements of a matrix by a divisor

    Args:
        matrix (list): matrix of numbers
        div (int): divisor to divide each matrix element
    """
    index = 0
    nCol = 0
    if matrix == []:
        return []
    if matrix is not None:
        nCol = len(matrix[0])
    else:
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")

    for i in matrix:
        if len(matrix[index]) != nCol:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not(type(j) is int or type(j) is float):
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
        index += 1

    if not (type(div) is int or type(div) is float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    row = []
    for i in matrix:
        for j in i:
            row.append(round(j / div, 2))
        result.append(row)
        row = []

    return result

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/2-matrix_divided.txt")
