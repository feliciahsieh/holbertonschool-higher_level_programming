#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square definition
    Methods:
        __init__()
        __str__()
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
