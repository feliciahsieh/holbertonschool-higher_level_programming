#!/usr/bin/python3


def remove_char_at(str, n):
    if n >= 0:
        result = str[0:n] + str[n+1:len(str)]
        return(result)
    else:
        return(str)

print(remove_char_at("Holberton School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))
