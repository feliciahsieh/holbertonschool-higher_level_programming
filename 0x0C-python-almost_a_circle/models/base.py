#!/usr/bin/python3


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ - initialize Base object
        Args
            id(int) - initialize obj with ID or use autonumber as ID
        Return:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
