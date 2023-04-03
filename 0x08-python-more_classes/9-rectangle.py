#!/usr/bin/python3
"""
Module that defines the Rectangle class
"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance given width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of this rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of this rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of this rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of this rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of this rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of this rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of this rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rect_str = ""
            for i in range(self.height):
                rect_str += str(self.print_symbol) * self.width + "\n"
            return rect_str[:-1]

    def __repr__(self):
        """Return a string representation of this rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when this rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size"""
        return cls(size, size)
