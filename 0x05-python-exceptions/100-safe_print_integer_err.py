#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    result = False
    try:
        print("{:d}".format(value))
        result = True
        return True
    except ValueError as err:
        sys.stderr.write("Exception: %sn" %str(err))
        return False
