#!/usr/bin/python3
"""
    define class Rectangle
"""


class Rectangle:
    """ Define Rectangle class

    Args:
        number_of_instances (int): count of number of instances

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize Rectangle instance
        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle
        """
        __dict__ = {}
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        # Getter
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
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        # Getter
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
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        area - Returns the area of the Rectangle instance
        Args:
            None
        """
        return self.height * self.width

    def perimeter(self):
        """
        perimeter - Returns the perimeter of the Rectangle instance
        Args:
            None
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """
        prints rectangle instance using # character

        Args:
            None
        """
        if self.width == 0 or self.height == 0:
            return ""
        rect = str(self.print_symbol) * self.width
        rect = (rect + "\n") * (self.height - 1) + rect
        return rect

    def __repr__(self):
        """
        returns rectangle instance using # character

        Args:
            None
        """
        if self.width == 0 or self.height == 0:
            return {}
        return "Rectangle({}, {})".format(self.width, self. height)

    def __del__(self):
        """
        __del__ - deletes instance of Rectangle instance

        Args:
            None
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
