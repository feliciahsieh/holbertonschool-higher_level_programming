#!/usr/bin/python3
"""
7-save_to_json_file.py / save_to_json_file - write object to a text file
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    # Always create the file
    with open(filename, 'w+') as f:
        pass

    if type(filename) is not str:
        return 0

    j = json.dumps(my_obj)

    with open(filename, "w+") as file:
        return file.write(j)
