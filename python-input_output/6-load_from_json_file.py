#!/usr/bin/python3
"""Module for creating objects from JSON file"""


import json


def load_from_json_file(filename):
    """creates and Object from a JSON"""
    with open(filename, "r", encoding="UTF8") as file:
        jstring = file.read()
    return json.loads(jstring)
