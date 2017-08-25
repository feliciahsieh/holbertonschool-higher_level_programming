#!/usr/bin/python3
"""
    add_integer: add two numbers together
"""


def add_integer(a, b):
    """ Add two numbers together, a and b

    Args:
    a (int): first operand
    b (int): second operand
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return(int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
