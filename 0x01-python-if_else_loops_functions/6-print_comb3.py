#!/usr/bin/python3
for y in range(0, 9):
    for x in range(y + 1, 10):
        if (y != 8 or x != 9):
            print ('{}'.format(y), '{}'.format(x), ", ", sep="", end="")
        else:
            print ('{}'.format(y), '{}'.format(x), sep="")
