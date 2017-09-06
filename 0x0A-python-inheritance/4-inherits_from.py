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
    if type(obj) in a_class.__subclasses__():
        return True
    return False
