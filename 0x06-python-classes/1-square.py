#!/usr/bin/python3
"""
This module defines the Square class, which is a square with a given size.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): A private instance attribute for the size of the square.
    """

    def __init__(self, size):
        """Initializes a new Square object.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
