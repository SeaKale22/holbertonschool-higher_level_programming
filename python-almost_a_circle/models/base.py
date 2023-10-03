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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string rep of list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json string to file"""
        file_name = cls.__name__ + ".json"
        if list_objs is not None:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        else:
            list_dict = []
        jstring = cls.to_json_string(list_dict)
        with open(file_name, "w") as f:
            f.write(jstring)
