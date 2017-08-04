#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    if count == 1:
        argu = "argument"
        punc = "."
        print("0 argument.")
        sys.exit(0)
    elif count == 2:
        argu = "argument"
        punc = ":"
    else:
        argu = "arguments"
        punc = ":"
    print('{:d} {:s}{:s}'.format(count - 1, argu, punc), sep="")
    for i in range(1, count):
        print('{:d}: {:s}'.format(i, sys.argv[i]))
