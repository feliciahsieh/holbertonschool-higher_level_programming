#!/usr/bin/python3
"""
7-save_to_json_file.py / save_to_json_file - write object to a text file
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file - writes object to text file using a JSON representation
    """

    if type(filename) is not str or filename == "":
        return 0
    jsonStr = json.dumps(my_obj)

    with open(filename, "w+") as f:
        return f.write(jsonStr)
