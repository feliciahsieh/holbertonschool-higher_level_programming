#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        #except Exception as e:
        #    print("hello\n", e)

    def area(self):
        return self.__size ** 2
