#!/usr/bin/python3
"""
Base class definition
"""
import json


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

    @staticmethod
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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - writes JSON string of list_objs to a file.
        Convert (Rectangle|Square obj) -> dictionary -> string of dict -> file.
        Args:
            cls() - class type of list_objs. Used to derive <ClassName>.json
            list_objs(list) - list of Base instances (Rectangle or Square)
        Return:
            None
        """

        #a = {}

        fs = ""
        l = []
        i = 0
        for obj in list_objs:
            s = Base.to_json_string(obj.to_dictionary())
            if (i != 0):
                fs = fs + ", " + s
            else:
                fs = "[" + s
                i = 1
            print(fs)
        fs = fs + "]"
        with open(str(cls.__name__) + ".json", "w+") as f:
            f.write(str(fs))
