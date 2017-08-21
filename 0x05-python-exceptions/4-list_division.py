#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = []
    for i in range(list_length):
        try:
            result = 0.0
            result = int(my_list_1[i]) / int(my_list_2[i])
        except (TypeError, ValueError):
            print("wrong type")
            continue
        except ZeroDivisionError:
            print("division by 0")
            continue
        except IndexError:
            print("out of range")
            continue
        finally:
            a.append(result)
    return a
