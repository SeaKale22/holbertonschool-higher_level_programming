#!/usr/bin/python3
"""Module for class_to_json"""


def class_to_json(obj):
    """Returns dictionary decrption of object"""
    json_dict = {}
    for attribute in dir(obj):
        if isinstance(attribute, (list, dict, str, int, bool)):
            json_dict[attribute] = getattr(obj, attribute)
    return json_dict