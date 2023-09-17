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

    def area(self):
        """Finds the area of the square.
        Returns: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size.
        Args:
            value- the value to set the size as
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print()
