#!/usr/bin/python3
"""Module to print a square"""


def print_square(size):
    """prints a square according to size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size miust be an integer")
    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()
