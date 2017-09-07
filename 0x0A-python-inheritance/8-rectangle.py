#!/usr/bin/python3
"""
    8-rectangle.py / class Rectangle
    Note: must use specia __import__ to get file due to hyphen problem
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle definition
    Args:
         None
    Return: None
    """
    def __init__(self, width, height):
        """
        __init__ - initialization of Rectangle class
        Args:
            None
        Return: None
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
