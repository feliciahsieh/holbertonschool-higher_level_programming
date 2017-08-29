#!/usr/bin/python3
"""
Define class Rectangle
"""


class Rectangle:
    """
    Define Rectangle class

    Args:
        width (int): width of the Rectangle
        height (int): height of the Rectangle

    Class variables:
        number_of_instances (int): count of number of instances
        print_symbol (string): single character to use to print the Rectangle

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle instance

        Args:
            width (int): width of Rectangle
            height (int): height of Rectangle

        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """

        Getter for width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """

        Set width of Rectangle instance

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
        """

        Getter for height

        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Set height of Rectangle instance

        Args:
            value (int): desired value of height of Rectangle

        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        bigger_or_equal - Returns the largest Rectangle by area

        Args:
            rect_1 (Rectangle): first Rectangle
            rect_2 (Rectangle): second Rectangle

        Return:
            The bigger Rectangle by area
        """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1 >= rect_2:
            return rect_1
        return rect_2

    def area(self):
        """
        area - Returns the area of the Rectangle instance

        Args:
            None
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        perimeter - Returns the perimeter of the Rectangle instance
        Args:
            None
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        prints rectangle instance using # character

        Args:
            None
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        rect = str(self.print_symbol) * self.__width
        rect = (rect + "\n") * (self.__height - 1) + rect
        return rect

    def __repr__(self):
        """
        returns rectangle instance using # character

        Args:
            None
        """
        w = self.__width
        h = self.__height
        return "Rectangle({}, {})".format(w, h)

    def __del__(self):
        """
        __del__ - deletes instance of Rectangle instance

        Args:
            None
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __le__(self, other):
        return self.area() <= other.area()
