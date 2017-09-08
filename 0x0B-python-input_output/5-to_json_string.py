#!/usr/bin/python3
"""
5-to_json_string.py / to_json_string(my_obj)
"""


import json


def to_json_string(my_obj):
    """
    to_json_string - returns the JSON representation of an object (string)
    Arg:
        my_obj (Unk): object
    Return:
        JSON representation of an object (string)
    """
    return json.dumps(my_obj)
