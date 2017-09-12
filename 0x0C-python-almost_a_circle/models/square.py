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
        return self.__width

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
        self.__width = value   # also value of size
        self.__height = value  # also value of size

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
        if len(args) > 0:
            l = ["id", "size", "x", "y"]
            d = {}
            index = 0
            for arg in args:
                d[l[index]] = arg
                index += 1
                self.__dict__.update(d)
        else:
            kd = {}
            for key, value in kwargs.items():
                kd[key] = value
                if key == "size":  # manually update value
                    self.width = value
                    self.height = value
                self.__dict__.update(kd)

    def to_dictionary(self):
        """
        to_dictionary - return the dictionary representation of a Square
        Args:
            None
        Return:
            custom dictionary of Square
        """
        d = {}
        d["id"] = self.id
        d["size"] = self.width
        d["x"] = self.x
        d["y"] = self.y

        return d
