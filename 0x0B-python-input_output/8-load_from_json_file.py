#!/usr/bin/python3
"""
8-load_from_json_file.py / load_from_json_file -
creates an Object from a "JSON file
"""

import json


def load_from_json_file(filename):
    """
    load_from_json_file - creates an Object from a "JSON file
    Args
        filename(str) - filename to read from
    Return
        None
    """
    if type(filename) is not str:
        return

    with open(filename, mode="r") as file:
        return json.loads(file.read())
