#!/usr/bin/python3
"""
    text_indentation: print 2 newlines instead of every period,
        question mark, or colon character.
"""


def text_indentation(text):
    """
    print 2 newlines instead of every period,
    question mark, or colon character.

    Args:
    text (str): string of text to format
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    isSkip = False
    for i in text:
        if isSkip is False:
            if i == '.' or i == '?' or i == ':':
                print(i, '\n' * 2, end="", sep="")
                isSkip = True
            else:
                print(i, end="", sep="")
        else:
            if i == ' ':
                continue
            else:
                print(i, end="")
                isSkip = False
