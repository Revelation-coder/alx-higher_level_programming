#!/usr/bin/python3
"""
This module defines a Square class for a square shape.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): A private instance attribute for the size of the square.

    Methods:
        __init__(self, size=0): Initializes new Square object given size.
    """
    pass

    def __init__(self, size=0):
        """
        Initializes a new Square object with a given size.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
