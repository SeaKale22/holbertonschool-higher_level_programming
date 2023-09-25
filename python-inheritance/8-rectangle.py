#!/usr/bin/python3
"""Module for rectangle"""


class BaseGeometry():
    """An incomplete class"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Represents a rectangle and inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initilization with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
