#!/usr/bin/python3
"""Module for lookup function"""


def lookup(obj):
    """Finds avalable attributes and methods of an object
    Param obj: The object to be searched
    Return: A list of attributes and methods for the object"""
    return dir(obj)
