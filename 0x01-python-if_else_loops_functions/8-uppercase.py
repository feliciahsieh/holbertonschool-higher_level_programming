#!/usr/bin/python3


def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            offset = ord('A') - ord('a')
        else:
            offset = 0
        print('{}'.format(chr(ord(i) + offset)), end="")
    print("")
