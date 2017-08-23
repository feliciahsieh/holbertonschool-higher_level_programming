#!/usr/bin/python3
import dis





class MagicClass:
    def __init__(self): #10
        self.__radius = 0 #11
        if type(radius) is not int and type(radius) is not float:
            return self.__radius == radius
        if type(self.__radius) == float:
            raise TypeError('radius must be a number')
    def area(self, radius):
        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        return  2 * math.pi * self.__radius

dis.dis(MagicClass)
