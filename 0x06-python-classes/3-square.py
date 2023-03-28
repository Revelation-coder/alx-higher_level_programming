#!/usr/bin/python3
"""
This module defines a Square class representing a square shape.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): A private instance attribute for the size of the square.

    Methods:
        area(): Returns the area of the Square object.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square object with a given size.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the Square object.

        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)
