#!/usr/bin/python3
""" square.py """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square definition
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

    @property
    def size(self):
        """ Getter for size (which is really width)"""
        return self.width

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
        self.width = value  # also value of size
        self.height = value

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

    def update(self, *args, **kwargs):
        """
        update - assigns attributes to Square
        Args:
            args - attributes as a series of arguments
            kwargs - attributes as a dictionary
        Return:
            None
        """
        kd = {}
        for key, value in kwargs.items():
            kd[key] = value
        if "size" in kwargs:
            kd['height'] = kd['size']
            kd['width'] = kd['size']
        self.__dict__.update(kd)

        l = ["id", "size", "x", "y"]
        d = {}
        index = 0
        for arg in args:
            d[l[index]] = arg
            index += 1
        if len(args) >= 2:
            d['height'] = d['size']
            d['width'] = d['size']
        self.__dict__.update(d)
