#!/usr/bin/python3
def magic_string(n):
    if n == 0:
        return ""
    return "Holberton, " * (n - 1) + "Holberton"
