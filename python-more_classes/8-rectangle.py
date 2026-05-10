#!/usr/bin/python3
"""Rectangle script"""


class Rectangle:
    """Class defined for this script"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        # Assignments of attributes
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        # width getter
        return self.__width

    @width.setter
    def width(self, value):
        # width setter
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        # height getter
        return self.__height

    @height.setter
    def height(self, value):
        # height setter
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        # computing the area
        return self.__width * self.__height

    def perimeter(self):
        # computing the perimeter
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        # preparing the print
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += "{}".format(self.print_symbol)
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        # actual return and printing
        return self._draw_rectangle()

    def __repr__(self):
        # format printing
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        # when deleted code
        cls.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        # doing comparison
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
