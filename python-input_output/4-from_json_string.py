#!/usr/bin/python3
"""Module for converting from JSON"""


import json


def from_json_string(my_str):
    """Returns an object represented by JSON"""
    return json.loads(my_str)
