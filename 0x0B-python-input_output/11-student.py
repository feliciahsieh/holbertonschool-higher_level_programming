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

    def to_json(self):
        """
        to_json - return dictionary of self
        Args:
            None
        Return:
            python dictionary of self
        """
        return self.__dict__
