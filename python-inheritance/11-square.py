#!/usr/bin/python3
"""Module for square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """initilizes square using super()"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns string rep of square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
