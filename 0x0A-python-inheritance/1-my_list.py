#!/usr/bin/python3
"""
    Define print_sorted() method
"""


class MyList(list):
    """
    Class MyList
    """

    def print_sorted(self):
        """
        print_sorted()
        Args:
            None
        """
        print(sorted(self))
