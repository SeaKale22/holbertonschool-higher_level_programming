#!/usr/bin/python3
"""Module for square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class for Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initilize the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string rep of square"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width,)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
