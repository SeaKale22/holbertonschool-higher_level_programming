#!/usr/bin/python3
"""Module for Rectangle"""


from models.base import Base


class Rectangle(Base):
    """class for Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initilization for Rectangle"""
        self.valid("width", width)
        self.valid("height", height)
        self.valid("x", x)
        self.valid("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.valid("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.valid("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.valid("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.valid("y", value)
        self.__y = value

    def valid(self, attrib_name, value):
        """validates attributes"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attrib_name))
        if attrib_name == "width" or attrib_name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(attrib_name))
        if attrib_name == "x" or attrib_name == "y":
            if value < 0:
                raise ValueError("{} msut be >= 0".format(attrib_name))

    def area(self):
        """Returns area of rectangle"""
        return self.__height * self.__width
    
    def display(self):
        for num in range(self.__height):
            for num in range(self.__width):
                print("#", end='')
            print()
