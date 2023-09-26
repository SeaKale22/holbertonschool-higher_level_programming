#!/usr/bin/python3
"""Module for load, add, save"""


import sys
import os
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]

if not os.path.exists("add_item.json"):
    add_list = arguments
    save_to_json_file(add_list, "add_item.json")
else:
    add_list = load_from_json_file("add_item.json")
    add_list.extend(arguments)
    save_to_json_file(add_list, "add_item.json")
