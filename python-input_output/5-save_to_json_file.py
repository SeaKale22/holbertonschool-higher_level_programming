#!/usr/bin/python3
"""Module for writing object to text file"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON"""
    json_object = json.dumps(my_obj)
    with open(filename, "w") as file:
        file.write(json_object)
