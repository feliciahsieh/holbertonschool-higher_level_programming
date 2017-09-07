#!/usr/bin/python3


class MyInt(int):
    """
    MyInt - class that inherits from int
    """
    def __eq__(self, other):
        """
        __eq__ - redefine == to !=
        Args:
            other - other operand
        Return:
            True if Not_Equal to
        """
        if self != other:
            return True
        return False

    def __ne__(self, other):
        """
        __ne__ - redefine != to ==
        Args:
            other - other operand
        Return:
            True if Equal to
        """
        if self == other:
            return True
        return False
