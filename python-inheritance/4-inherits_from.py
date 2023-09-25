#!/usr/bin/python3
"""Module for inherits_from"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that inherits from a_class
    Param obj: the object to check
    Param a_class: the class to check
    Returns: True if obj is an instance of a class that inherits from a_class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
