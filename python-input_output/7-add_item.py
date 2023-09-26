#!/usr/bin/python3
"""Module for load, add, save"""


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]

add_list = load_from_json_file("add_item.json")
add_list.append(arguments)
save_to_json_file(add_list, "add_item.json")
