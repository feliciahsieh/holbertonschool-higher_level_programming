#!/usr/bin/python3
"""
4-append_write.py / append_write
"""


def append_write(filename="", text=""):
    """
    append_write - appends a string at the end of a text file (UTF8)
    Arg
        filename(str) - filename to append to
        text(str) - string to append to file
    Return
        the number of characters added:
    """
    count = 0

    if type(filename) is not str or type(text) is not str:
        return 0

    with open(filename, mode="a", encoding="utf-8") as f:
        count = f.write(text)
        return count
