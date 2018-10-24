#!/usr/bin/python3


def add_attribute(self, key, value):
    """
    add_attribute - add new attribute to object, else raise TypeError
    Args:
        key: new attribute name
        value: new attribute value
    Returns:
        nothing
    """
    if type(self) is not int and type(self) is not float \
       and type(self) is not str:
        setattr(self, key, value)
    else:
        raise TypeError("can't add new attribute")
