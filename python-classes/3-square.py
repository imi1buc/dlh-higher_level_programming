#!/usr/bin/python3
"""This script creates a class Square, assign the size attribute to it
and then returns the area after some type and value validations"""


class Square:
    """"This class checks the type and value of size
    and then returns the area"""

    def __init__(self, size=0):
        # Testing the type of the attribute size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        # Determining the area
        return self.__size ** 2
