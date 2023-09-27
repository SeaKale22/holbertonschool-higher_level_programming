#!/usr/bin/python3
"""Module for Student class"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initilizes student with first_name, last_name, and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of student"""
        json_dict = {}
        for attribute in self.__dict__:
            attribute_value = getattr(self, attribute)
            if isinstance(attribute_value, (list, dict, str, int, bool)):
                json_dict[attribute] = attribute_value
        return json_dict
