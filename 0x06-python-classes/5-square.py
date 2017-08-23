#!/usr/bin/python3
import sys


class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    sys.stdout.write('#')
                sys.stdout.write('\n')
        else:
            sys.stdout.write('\n')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value=0):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
