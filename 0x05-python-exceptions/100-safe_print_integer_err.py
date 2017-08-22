#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    result = False
    try:
        print("{:d}".format(value))
    except ValueError as err:
        sys.stderr.write("Exception: {}\n".format(str(err)))
    except TypeError as err:
        sys.stderr.write("Exception: {}\n".format(str(err)))
    else:
        result = True
    finally:
        return result
