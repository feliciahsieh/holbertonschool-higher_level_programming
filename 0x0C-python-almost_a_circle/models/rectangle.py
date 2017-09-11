#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle definition
    """

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
        """ Setter for __x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
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
        if value < 0:
            raise ValueError("y must be >= 0")
        self.y = value

    def area(self):
        """
        area - calculates the area of a Rectangle
        Args:
            None
        Return:
            None
        """
        return self.width * self.height

    def display(self):
        """
        display - prints the Rectangle to the screen using a character
        Args:
            None
        Return:
            None
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, "#" * self.width, "\n", end="", sep="")

    def __str__(self):
        """
        ___str__ - overload the ___str___ method with the format:
[Rectangle] (<id>) <x>/<y> - <width>/<height>
        Args:
            None
        Return:
            None
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        update - update Rectangle instance with variatic attributes
        Args:
            args(unk) - random ordered list of attributes
            kwargs(unk) - random dictionary attributes
        Return:
            None
        """
        if len(args) > 0:
            l = ["id", "width", "height", "x", "y"]
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
                self.__dict__.update(kd)

    def to_dictionary(self):
        """
        to_dictionary - return the dictionary representation of a Rectangle
        Args:
            None
        Return:
            None
        """
        return self.__dict__
