#!/usr/bin/python3
class Node:
    def __init__(self, data=0, next_node=None):
        __data = n
        __next_node = None
        if type(data) == int:
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if value == None or type(value) == type(Node):
            self.__next_node = next_node
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value == None or type(value) == type(Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head
        self.next_node = None

    def __str__(self):
        curr = self.__head
        while (curr != None):
            print(curr.__head.data)
            curr = curr->next_node

    def sorted_insert(self, value):
        
