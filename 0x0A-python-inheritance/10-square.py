#!/usr/bin/python3
"""
    10-square class
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

    def __init__(self, size):
        """
        __init__ - initialization of Square class
        Args:
            None
        Return: None
        """

        try:
            if self.integer_validator("size", size) and size >= 0:
                super().__init__(size, size)
                self.__size = size
        except Exception as e:
            raise e.__class__(e)

    def area(self):
        """
        area - calculates area of Square
        Args:
             None
        Returns:
             Area of Square
        """
        return self.__size * self.__size
