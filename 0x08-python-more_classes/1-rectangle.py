#!/usr/bin/python3
"""
    define class Rectangle
"""


class Rectangle:
    """ Define Rectangle class

    Args:
        None
    """

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle instance

        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Get width of Rectangle instance

        Args:
            None

        Returns:
            Width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width of Rectangle instance

        Args:
            value (int): desired value of width of Rectangle
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get height of Rectangle instance

        Args:
            None

        Returns:
            Height of Rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height of Rectangle instance

        Args:
            value (int): desired value of height of Rectangle
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
