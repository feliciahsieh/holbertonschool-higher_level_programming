#!/usr/bin/python3
def matrix_divided(matrix, div):
    index = 0
    nCol = 0
    if matrix is not None:
        nCol = len(matrix[0])
    for i in matrix:
        if len(matrix[index]) != nCol:
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
        index += 1

    if type(div) is not int and type(div) is not float:
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
