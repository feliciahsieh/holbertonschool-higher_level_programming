#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    result = False
    try:
        print("{:d}".format(value))
        result = True
    except ValueError as err:
        sys.stderr.write("Exception: %s\n" %str(err))
    finally:
        return result
