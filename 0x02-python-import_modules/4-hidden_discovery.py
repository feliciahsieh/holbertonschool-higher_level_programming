#!/usr/bin/python3

if __name__ == "__main__":
    import re
    import hidden_4
    regex = r"__"
    for i in dir(hidden_4):
        if i[:2] != "__":
            print('{:s}'.format(i))
