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
        if type(size) != int and type(size) != float:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of a Square instance and check for Exceptions

        Args:
        None

        """
        return self.__size ** 2

    @property
    def size(self):
        """ Getter for size """
        return self.__size

    @size.setter
    def size(self, value=0):
        """ Setter for size """
        if type(value) != int and type(value) != float:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        return self.__size == other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __le__(self, other):
        return self.__size <= other.__size
