#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """
    append_after - inserts a line of text to a file after each line
    containing a specific string
    Args:
        filename(str) - filename to process
        search_string(str) - string to search within file
        new_string(str) - string to add after a line matches search_string
    Return:
        None (Change file to reflect changes)
    """
    contentsCopy = []
    with open(filename, "r") as f:
        contents = f.readlines()

        for i in range(len(contents)):
            contentsCopy.append(contents[i])
            if search_string in contents[i]:
                contentsCopy.append(new_string)

    with open(filename, "w+") as f:
        c = "".join(contentsCopy)
        f.write(c)
