#!/usr/bin/python3
"""This script creates a class Square, assign the size attribute to it
and then returns the area after some type and value validations"""


class Square:
    """"This class checks the type and value of size
    and then returns the area"""

    def __init__(self, size=0):
        # Initializes the square
        self.size = size

    @property
    def size(self):
        # Retrieves the size
        return self.__size

    @size.setter
    def size(self, value):
        # Testing the type of the attribute size
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        # Determining the area
        return self.__size ** 2
