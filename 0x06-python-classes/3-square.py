#!/usr/bin/python3
class Square:
    """Initialize Square class instance with size

    Attributes:
        None:

    """

    def __init__(self, size=0):
        """Initialize Square class instance with size and check for Exceptions

        Size must be a positive and valid number.

        Args:
        size (int): size of the side of a Square class

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of a Square instance and check for Exceptions

        Args:
            None

        """
        return self.__size ** 2
