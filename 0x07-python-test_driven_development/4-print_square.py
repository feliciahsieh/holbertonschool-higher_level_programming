#!/usr/bin/python3
"""
    print_square: prints a square of # characters
"""


def print_square(size):
    """
    prints a square of # characters

    Args:
        size (int): number of columns of # character

    """

    if type(size) is float and size < 0.0:
        raise TypeError("size must be an integer")

    if size == None or type(size) is str or type(size) is tuple:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        if size < 0 or size < 0.0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * int(size))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
