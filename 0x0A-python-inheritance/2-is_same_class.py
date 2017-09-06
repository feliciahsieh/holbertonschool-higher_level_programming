#!/usr/bin/python3
"""
    2-is_same_class.py / is_same_class() module
"""


def is_same_class(obj, a_class):
    """
    is_same_class method
    Args:
        obj (obj): object to inspect
        a_class(classname): class to check
    Returns: True if obj is an instance of a_class. Else False
    """
    if type(obj) == a_class:
        return True
    return False
