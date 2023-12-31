#!/usr/bin/python3
"""This modual contains a square"""


class Square:
    """Represets a square"""
    def __init__(self, size=0):
        """Instantiation with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
