#!/usr/bin/python3
offset = 0
for i in range(25, -1, -1):
    if i % 2 == 0:
        offset = ord('A') - ord('a')
    else:
        offset = 0
    print('{}'.format(chr(i + ord('a') + offset)), end="")
