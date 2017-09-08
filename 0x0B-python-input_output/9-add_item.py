#!/bin/usr/python3
"""
9-add_item.py - adds all arguments to a Python list, and save them to a file.
Uses:
save_to_json_file from 7-save_to_json_file.py and
load_from_json_file from 8-load_from_json_file.py
"""

import sys
import json


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
fname = "add_item.json"

with open('add_item.json', 'a+') as f:
    pass

listObj = []
listObj = load_from_json_file(fname)

#print(listObj)
#for i in range(1, len(sys.argv)):
#    listObj.append(sys.argv[i])

#save_to_json_file(listObj, fname)
