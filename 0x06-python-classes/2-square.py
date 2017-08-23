#!/usr/bin/python3
class Square:
    """Initialize Square class instance with size

    Attributes:
        None:

    """

    def __init__(self, size=0):
        """Initialize Square class instance with size and check for Exceptions

        Args:
        size (int): size of the side of a Square class
        dict (dict): dictionary in a Square class

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
