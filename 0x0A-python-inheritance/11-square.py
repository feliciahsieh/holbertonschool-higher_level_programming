#!/usr/bin/python3
"""
    11-square class
    Note: must use specia __import__ to get file due to hyphen problem
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square definition
    Args:
         None
    Return: None
    """

    __size = 0

    def __init__(self, size):
        """
        __init__ - initialization of Square class
        Args:
            None
        Return: None
        """

        if size > 0:
            self.integer_validator("size", size)
            super().__init__(size, size)
            self.__size = size

    def area(self):
        """
        area - calculates area of Square
        Args:
             None
        Returns:
             Area of Square
        """
        return self.__size * self.__size

    def print(self):
        """
        print - print the Rectangle area
        Arg:
            None
        Return: area of Rectangle
        """
        return self.area

    def __str__(self):
        """
        __str__ - print the formal Square data
        Arg:
            None
        Return: string describing area
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
