#!/usr/bin/python3
"""This modual contains a square"""


class Square:
    """Represets a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with size and position"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if (
            not isinstance(position, tuple)
            and len(position) != 2
            and not
            all(isinstance(element, int)
                and element < 0 for element in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method for position"""
        if (
            not isinstance(value, tuple)
            and len(value) != 2
            and not all
            (isinstance(element, int)
                and element < 0 for element in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
