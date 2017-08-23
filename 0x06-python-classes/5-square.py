#!/usr/bin/python3
"""
Square class methods and strings
"""

class Square:
    """Square methods and vars

    Attributes:
        size (int): size of Square instance

    """

    def __init__(self, size=0):
        """Initialize Square class instance with size and check for Exceptions

        Args:
            self (Square): The Square instance
            size (int): size of the side of a Square class

        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of a Square instance

        Args:
            self (Square): square instance

        Returns:
            area of the square

        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter for size

        Args:
            self (Square): The square instance

        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value=0):
        """
        Setter for size

        Args:
            self (Square): The square instance
            value (int): size of __size var

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints a square made up of #'s

        Args:
            self (Square): The Square instance

        Returns:
            None
        """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#')
                print('\n')
        else:
            print('\n')
