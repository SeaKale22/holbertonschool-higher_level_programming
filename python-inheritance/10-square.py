#!/usr/bin/python3
"""Module for square"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square"""


    def __init__(self, size):
        """initilizes square using super()"""
        self.integer_validator("size", size)
        super().__init__(size, size)
