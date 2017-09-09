#!/usr/bin/python3
class Student:
    """
    Student class definition
    Member:
        first_name (str) - first name of student
        last_name (str) - last name of student
        age (int) - age of student
    """

    def __init__(self, first_name, last_name, age):
        """
        __init__ - initialization of class instance
        Args:
            first_name(str) - first name of student
            last_name(str) - last name of student
            age(int) - age of student
        Return:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        to_json - return dictionary of self
        Args:
            None
        Return:
            python dictionary of self
        """

        d = {}

        if attrs is not None:
            for k in self.__dict__.keys():
                #print("key", k, "value", self.__dict__[k])
                for a in range(len(attrs)):
                    if attrs[a] == k:
                        d[k] = self.__dict__[k]
        else:
            for k in self.__dict__.keys():
                if type(k) == str:
                    d[k] = self.__dict__[k]
        return d
