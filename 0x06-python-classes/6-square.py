#!/usr/bin/python3
import sys


class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] >= 0 and position[1] >= 0 and len(position) == 2:
            self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size != 0:
            for y in range(self.__position[1]):
                sys.stdout.write('\n')
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    sys.stdout.write(' ')
                for j in range(self.__size):
                    sys.stdout.write('#')
                sys.stdout.write('\n')
        else:
            sys.stdout.write('\n')

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] > 0 and value[1] > 0 and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
