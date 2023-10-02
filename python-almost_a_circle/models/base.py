#!/usr/bin/python3
"""Module for base class"""


class Base:
    """Base class for other project classes"""
    __nb_objects = 0
    def __init__(self, id =None):
        """Initalization with optional id"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects