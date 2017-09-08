#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    number_of_lines - returns the number of lines of a text file
    Args:
        filename(str) - filename to open
    Returns:
        number of lines in the file
    """
    i = 0

    if type(filename) is not str:
        raise TypeError("filename is not a string")

    with open(filename, mode="r") as f:
        for i, l in enumerate(f):
            pass
    f.close()

    return i + 1
