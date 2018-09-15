#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
        if isinstance(data, int):
            self.__data = data
            if next_node is None or isinstance(next_node, Node):
                self.__next_node = next_node
            else:
                raise TypeError("next_node must be a Node object")
        else:
            raise TypeError("data must be an integer")

    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        t = ""
        curr = self.__head
        while curr is not None:
            t = t + str(curr.data) + "\n"
            curr = curr.next_node
        t = t[:-1]
        return t

    def sorted_insert(self, value):
        n = Node(value)

        # Very First node
        if self.__head is None:
            self.__head = n
            return

        curr = self.__head

        # New First node
        if n.data <= curr.data:
            n.next_node = self.__head
            self.__head = n
            return

        # Multiple nodes
        while curr.next_node is not None and curr.next_node.data < n.data:
            curr = curr.next_node

        n.next_node = curr.next_node
        curr.next_node = n
