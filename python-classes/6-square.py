#!/usr/bin/python3
"""Square, size and position script"""


class Square:
    """Class defined for this script"""

    def __init__(self, size=0, position=(0, 0)):
        # Assignments of attributes
        self.size = size
        self.position = position

    @property
    def size(self):
        # size getter
        return self.__size

    @size.setter
    def size(self, value):
        # size setter
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        # position getter
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in value:
            if type(i) is not int or i < 0:
                raise TypeError('position must be a tuple of ' +
                                '2 positive integers')
        self.__position = value

    def area(self):
        # Determining the area
        return self.__size ** 2

    def my_print(self):
        # Printing the response
        if self.__size == 0:
            print()
        else:
            for val in range(0, self.__position[1]):
                print()
            for row in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for col in range(0, self.__size):
                    print("#", end="")
                print()
