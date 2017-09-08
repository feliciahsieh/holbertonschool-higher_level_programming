#!/usr/bin/python3
import json
"""
6-from_json_string.py / from_json_string - return a Python object
from a JSON string
"""


def from_json_string(my_str):
    """
    from_json_string
    Args
        my_str(unk): json stiing to decode into object
    Return
        object version of json string
    """
    return json.loads(my_str)
