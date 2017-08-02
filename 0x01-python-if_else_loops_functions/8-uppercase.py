#!/usr/bin/python3
def uppercase(str):
    offset = ord('A') - ord('a')
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            print('{}'.format(chr(ord(i) + offset)), end="")
        else:
            print(i, end="")
    print("")
