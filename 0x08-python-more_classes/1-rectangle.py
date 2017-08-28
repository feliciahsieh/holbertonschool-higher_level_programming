#!/usr/python3
"""
    define class Rectangle
"""


class Rectangle:
    """ Define Rectangle class

    Args:
        None
    """

    def __init__(self, width=0, height=0):
        """ Initialize Rectangle instance
        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
        """
        __dict__ = {}
        self.width = width
        self.height = height

    @property
    def width(self):
        #Getter
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width of Rectangle instance
        Args:
            value (int): desired value of width of Rectangle
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        #Getter
        return self.__height

    @height.setter
    def height(self, value):
        """ Set height of Rectangle instance
        Args:
            value (int): desired value of height of Rectangle
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

#if __name__ == "__main__":
#    from 0-rectangle import Rectangle
