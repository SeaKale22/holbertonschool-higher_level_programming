#!/usr/bin/python3
"""Module for rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Represents a rectangle and inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initilization with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
