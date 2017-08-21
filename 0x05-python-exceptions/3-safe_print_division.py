#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = 0.0
        print("Inside result: ", end="")
        result = int(a) / int(b)
    except ZeroDivisionError:
        result = None
    except:
        pass
    finally:
        print("{}".format(result))
        return result
