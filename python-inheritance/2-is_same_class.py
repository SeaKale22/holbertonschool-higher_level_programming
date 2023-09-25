#!/usr/bin/python3
"""Module for checking if same class"""


def is_same_class(obj, a_class):
    """Determins if obj is an instance of a_class
    Param obj: The object ti be checked
    Param a_class: The class to check the object as
    Return: True if obj is exactly an instance of a_class, else false
    """
    if type(obj) == a_class:
        return True
    else:
        return False
