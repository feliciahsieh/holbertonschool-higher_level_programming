#!/usr/bin/python3
"""
Some text

"""


class MagicClass:
    def __init__(self):
        radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        if radius == self.__radius:
            return None

    def area(self, radius):
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        return 2 * math.pi * self.__radius
