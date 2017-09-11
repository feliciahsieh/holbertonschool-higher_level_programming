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
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        to_json_string - return JSON string of list_dictionaries
        Args:
            list_dictionaries(list) - list of dictionaries items
        Return:
            JSON string of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return str(list_dictionaries)
