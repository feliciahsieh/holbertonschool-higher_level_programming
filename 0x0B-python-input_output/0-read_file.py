#!/usr/bin/python3


def read_file(filename=""):
    """
    read_file - reads a text file with UTF8 encoding and prints it to stdout

    Args:
        filename(str): filename to open
    Returns
        None
    """

    with open(filename, mode="r", encoding="UTF8") as f:
        for line in f:
            print(line, end="")
