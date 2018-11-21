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

        return json.dumps(list_dictionaries)

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
        myList = []
        if list_objs:
            for obj in list_objs:
                myList.append(obj.to_dictionary())
        s = cls.to_json_string(myList)

        with open(str(cls.__name__) + ".json", "w") as f:
            f.write(s)

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

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create - returns an instance with all attributes already set
        Args:
            cls (class) - class of method
            dictionary(dict) - double pointer to a dictionary
        Result:
            An instance with all attributes
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)

        obj.update(**dictionary)

        return(obj)

    @classmethod
    def load_from_file(cls):
        """
        load_from_file - returns list of instances
        Args:
            None
        Return:
            list of instances
        """
        fn = str(cls.__name__) + ".json"
        import os.path
        if not os.path.isfile(fn):
            return []

        with open(fn, "r") as f:
            # read file text as string
            jsonStr = f.read()

            # convert to list of dictionaries
            jsonStr = cls.from_json_string(jsonStr)

            myList = []
            # convert list of objects (with dictionary data)
            for dictionary in jsonStr:
                obj = cls.create(**dictionary)
                myList.append(obj)
            return myList
