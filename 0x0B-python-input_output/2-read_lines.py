#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """
    read_lines - reads n lines of a text file (UTF8) and prints it to stdout
    """

    if type(filename) is not str or type(nb_lines) is not int:
        return

    listText = []
    with open(filename, mode="r") as f:
        for nLines, l in enumerate(f):
            listText.append(l)
    nLines + 1

    if nb_lines <= 0 or nb_lines >= nLines:
        for i in range(nLines):
            print(listText[i], end="")
    else:
        for i in range(nb_lines):
            print(listText[i], end="")
