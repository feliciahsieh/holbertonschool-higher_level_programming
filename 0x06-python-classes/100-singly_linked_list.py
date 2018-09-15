#!/usr/bin/python3
class Node:
    """Initialze Node class instance of singly-linked list
    Args:
        data (int): content of node
        next_node (Node): link to next node or None
    """
    def __init__(self, data=0, next_node=None):
        __data = n
        __next_node = None
        if type(data) == int:
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if value is None or type(value) == type(Node):
            self.__next_node = next_node
            raise TypeError("next_node must be a Node object")

    """ Getter for node content """
    @property
    def data(self):
        return self.__data

    """ Setter for node content """
    @data.setter
    def data(self, value):
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    """ Getter for next node link """
    @property
    def next_node(self):
        return self.__next_node

    """ Setter for next node link """
    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) == type(Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Initialize Singly Linked List
    Args:
        data (int): content of node
        next_node (Node): link to next node or None
    """
    def __init__(self):
        self.__head
        self.next_node = None

    def __str__(self):
        curr = self.__head
        while (curr is not None):
            print(curr.__head.data)
            curr = curr->next_node

    def sorted_insert(self, value):
        n = Node(value)

        # FIRST node in list
        if self.__head is None:
            self.__head = n

        # First NEW node in list
        if n.data <= self.__head.data:
            n.next_node = self.__head
            self.__head = n

        curr = self.__head
        # Find place after to be inserted
        while curr.next_node is not None and n.data < self.__head.data:
            curr = curr.next_node
        n.next_node = curr.next_node
        curr.next_node = n
