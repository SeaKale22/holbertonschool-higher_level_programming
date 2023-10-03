#!/usr/bin/python3
"""Module for base class"""


import json


class Base:

    """Base class for other project classes"""
    __nb_objects = 0

    def __init__(self, id=None):

        """Initalization with optional id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns json string rep of list of dictionaries"""
        if list_dictionaries is not None or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
