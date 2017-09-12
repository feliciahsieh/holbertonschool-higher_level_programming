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

        d = {}
        l = []
        for obj in list_objs:
            l.append(obj.to_dictionary())
        s = Base.to_json_string(l)
        with open(str(cls.__name__) + ".json", "w+") as f:
            f.write(str(s))

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string - returns the list of the JSON string
        Args:
            json_string(str) - string of list of dictionaries
        Return:
            Empty list if no JSON string or a list created from json_string
        """
        if json_string is None or json_string == "":
            return []

        print("json_string", json_string)

        d = json.loads(json_string)
        print("d", d)
        #for myList in d:
        #    for key, value in myList.iteritems():
        #        print(key, value)
        return d
