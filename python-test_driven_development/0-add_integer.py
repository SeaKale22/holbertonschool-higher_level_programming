#!/usr/bin/python3
"""module for add function"""


def add_integer(a, b=98):
    """
    Add two numbers
    param a: first int
    param b: second int, defult 98
    raises: TypeError if a or b are not an int or float
    return: the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
