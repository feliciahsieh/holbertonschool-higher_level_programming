#!/usr/bin/python3
"""
1-number_of_lines.py / number_of_lines()
returns the number of lines of a text file
"""

def number_of_lines(filename=""):
    """
    number_of_lines - returns the number of lines of a text file
    Args:
        filename(str) - filename to open
    Returns:
        number of lines in the file
    """
    i = 0

    if type(filename) is not str or filename == "":
        return 0

    with open(filename, mode="r", encoding="utf-8") as f:
        for i, l in enumerate(f):
            pass
    f.close()

    return i + 1
