#!/usr/bin/python3
"""Module for is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """checks if obj is or is an isntacnce of a class that inherits a_class
    Param obj: The object to check
    Param a_class: The class to check
    Returns: True if obj is instance a_class else False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
