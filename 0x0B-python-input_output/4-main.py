#!/usr/bin/python3
append_write = __import__('test').append_write

nb_characters_added = append_write(
    "file_append.txt", "Holberton School is so cool!\n")
print(nb_characters_added)
