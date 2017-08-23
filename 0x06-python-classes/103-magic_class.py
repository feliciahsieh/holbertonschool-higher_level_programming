#!/usr/bin/python3
import dis



class MagicClass:
    def __init__(self):
        if type(self.__radius) == int:
            pass
        if type(self.__radius) == float:
            pass


    def area(self, radius):
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        return  2 * math.pi * self.__radius

dis.dis(MagicClass)
