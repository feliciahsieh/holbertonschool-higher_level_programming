#!/usr/bin/python3


def remove_char_at(str, n):
    if n >= 0:
        result = str[0:n] + str[n+1:len(str)]
        return(result)
    else:
        return(str)
