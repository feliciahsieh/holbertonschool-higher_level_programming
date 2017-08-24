#!/usr/bin/python3
class Node:
    def __init__(self, n=0):
        __data = n

    @property
    def data(self):
        """
        Getter for data

        Args:
            self (Square): The square instance

        Returns:
            size of square
        """
        return self.__data
