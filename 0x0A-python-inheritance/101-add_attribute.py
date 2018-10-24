#!/usr/bin/python3


def add_attribute(obj, attr, value):
    """
    add_attribute - add new attribute to object, else raise TypeError
    Args:
        key: new attribute name
        value: new attribute value
    Returns:
        nothing
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
