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
    
    def update(self, *args, **kwargs):
        """Updates square by assigning argument to each attribute"""
        if not args:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                    self.height = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
