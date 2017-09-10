#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        ___init__ - initialize Rectangle object
        Vars:
            width(int) - width of Rectangle
            height(int) - height of Rectangle
            x(int) - x position of Rectangle
            y(int) - y position of Rectangle
        Result:
            None
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def __width(self):
        """ Getter for __width """
        return self.width

    @__width.setter
    def __width(self, value):
        """ Setter for __width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    @property
    def __height(self):
        """ Getter for __height """
        return self.height

    @__height.setter
    def __height(self, value):
        """ Setter for __height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.height = value

    @property
    def __x(self):
        """ Getter for __x """
        return self.x

    @__x.setter
    def __x(self, value):
        """ Setter for __y """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.x = value

    @property
    def __y(self):
        """ Getter for __y """
        return self.y

    @__y.setter
    def __y(self, value):
        """ Setter for __y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.y = value
