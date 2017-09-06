#!/usr/bin/python3
"""
    8-rectangle.py / class Rectangle
    Note: must use specia __import__ to get file due to hyphen problem
"""
BaseGeometry = __import__('7-base_geometry')


class Rectangle(BaseGeometry):
    """
    class Rectangle definition
    Args:
         None
    Return: None
    """
    def __init__(self, width, height):
        """
        __init__ - initialization of BaseGeometry class
        Args:
            None
        Return: None
        """
        self.__width = width
        self.__height = height

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
