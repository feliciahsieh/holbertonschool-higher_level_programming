#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except Exception as e:
        print("Inside result: {}".format(result))
    finally:
        return result
