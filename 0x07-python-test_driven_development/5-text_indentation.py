#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    isSkip = False
    for i in text:

        if i == '.' or i == '?' or i == ':':
            print(i, '\n' * 2, end="", sep="")
            isSkip = True
        else:
            if i == ' ' and isSkip:
                continue
            else:
                print(i, end="", sep="")
                isSkip = False

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
