#!/usr/bin/python3
"""Module for rectangle"""


class Rectangle:
    """Represents a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initilization with width and height"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height
            Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = ""
        for x in range(self.__height):
            rect_str += "#" * self.__width + "\n"
        return rect_str[:-1]

    def __repr__(self):
        """Returns a string representation that can recreate the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Preforms on instance Rectangle deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
