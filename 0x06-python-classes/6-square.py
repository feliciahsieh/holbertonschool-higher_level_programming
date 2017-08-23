#!/usr/bin/python3


class Square:
    """Initialize Square class instance with size

    Attributes:
        None:

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square class instance with size and check for Exceptions

        Size must be a positive and valid number.

        Args:
            size (int): size of the side of a Square class

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] >= 0 and position[1] >= 0 and len(position) == 2:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the area of a Square instance and check for Exceptions

        Args:
            None

        """
        return self.__size ** 2

    def my_print(self):
        """ Prints a square made up of #'s

        Args:
            None

        """
        if self.__size != 0:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end="")
                for j in range(self.__size):
                    print('#', end="")
                print()
        else:
            print()

    @property
    def size(self):
        """ Getter for size """
        return self.__size

    @property
    def position(self):
        """ Getter for position """
        return self.__position

    @size.setter
    def size(self, value):
        """ Setter for size """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ Setter for position """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] > 0 and value[1] > 0 and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
