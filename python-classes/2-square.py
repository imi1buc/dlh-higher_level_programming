#!/usr/bin/python3
"""This script creates another example of classes"""


class Square:
    """This class will work with attribute size and raise some exceptions"""
    def __init__(self, size=0):
        # Testing the type of the attribute size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
