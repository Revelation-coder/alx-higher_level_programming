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
        __init__(self, size=0): Initializes new Square object with given size.
        area(self): Returns the area of the Square object.
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
        self.size = size

    @property
    def size(self):
        """
        Getter method to get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Setter method to set the size of the square.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.size * self.size)
