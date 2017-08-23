#!/usr/bin/python3
"""Square class methods and strings.

Some stuff

"""

import sys


class Square:
    """Square methods and vars

    Some more text

    Attributes:
        size: (int): size of Square instance

    """

    def __init__(self, size=0):
        """Initialize Square class instance with size and check for Exceptions

        The __init__ method for Square.
        size must be a positive and valid number.

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

        Calc Square area

        """
        return self.__size ** 2

    def my_print(self):
        """ Prints a square made up of #'s

        Args:
            None

        """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    sys.stdout.write('#')
                sys.stdout.write('\n')
        else:
            sys.stdout.write('\n')

    @property
    def size(self):
        """ Getter for size """
        return self.__size

    @size.setter
    def size(self, value=0):
        """ int: size of Square """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
