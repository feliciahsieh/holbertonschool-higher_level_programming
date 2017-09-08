#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    write_file - writes a string to a text file (UTF8)
    Args:
        filename(str) - filename to write to
        text(str) - string to write to file
    Return:
        number of chars written
    """
    if type(filename) is not str or type(text) is not str:
        return 0

    with open(filename, mode="w", encoding="UTF8") as f:
        return f.write(text)
