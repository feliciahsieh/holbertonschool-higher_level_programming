#!/usr/bin/python3
"""
    7-base_geometry.py
"""


class BaseGeometry():
    """
    class BaseGeometry definition
    Args:
         None
    Return: None
    """
    def __init__(self):
        """
        __init__ - initialization of BaseGeometry class
        Args:
            None
        Return: None
        """
        pass

    def area(self):
        """
        area - raises Exception when method is called
        Args:
            None
        Return: None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator - verify value is an integer > 0
        Args:
            name (str): variable name
            value (int): value to store
        Return: None
        """
        if name is None or value is None:
            return False
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return True
