#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    4-inherits_from.py / inherits_from
    Args:
        obj (object): object to inspect
        a_class (classname): class to match
    Returns:
        True if the object is an instance of a class that inherited (directly
        or indirectly) from the specified class; otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
