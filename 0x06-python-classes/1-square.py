#!/usr/bin/pytho3
"""
This module defines the Square class, which represents a square with a given size.
"""

class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): A private instance attribute representing the size of the square.
    """

    def __init__(self, size):
        """Initializes a new Square object.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
