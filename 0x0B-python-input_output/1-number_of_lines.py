#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    number_of_lines - returns the number of lines of a text file
    Args:
        filename(str) - filename to open
    Returns:
        number of lines in the file
    """

    if type(filename) is not str:
        return 0

    with open(filename, mode="r") as f:
        for i, l in enumerate(f):
            pass
    return i + 1
