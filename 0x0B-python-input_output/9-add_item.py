#!/usr/bin/python3
import os
import sys

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
fname = "add_item.json"


with open(fname, 'a+') as f:
    pass

if os.stat(fname).st_size == 0:
    listObj = []
else:
    listObj = load_from_json_file(fname)

for i in range(1, len(sys.argv)):
    listObj.append(sys.argv[i])

save_to_json_file(listObj, fname)
