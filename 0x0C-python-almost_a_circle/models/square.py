#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square definition
    Methods:
        __init__()
        __str__()
        __size()
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ - initialize Square instance
        Args:
            size(int): size of square
            x(int): x coordinate of square
            y(int): y coordinate of square
            id(id): id of square
        Return:
            None
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """ Getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size(value) - Setter for size
        Args:
            value(int) - size of Square
        Return:
            None
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
        self.__size = value

    def __str__(self):
        """
        __str__ - print details of square instance
        Args:
            None
        Return
            None
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
