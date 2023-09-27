#!/usr/bin/python3
"""Module for class_to_json"""


def class_to_json(obj):
    """Returns dictionary decrption of object"""
    json_dict = {}
    for attribute in obj.__dict__:
        attribute_value = getattr(obj, attribute)
        if isinstance(attribute_value, (list, dict, str, int, bool)):
            json_dict[attribute] = attribute_value
    return json_dict