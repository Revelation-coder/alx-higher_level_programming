#!/usr/bin/python3
"""Module containing Square class"""


class Square:
    '''Class representing a square shape'''

    def __init__(self, size=0):
        '''Initializes a new Square object with a specified size.

        Args:
            size (int): The size of the square.
        '''
        self.size = size

    @property
    def size(self):
        '''Getter method for size attribute.'''
        return self.__size

    @size.setter
    def size(self, size):
        '''Setter method for size attribute.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Returns the area of the square.'''
        return (self.size * self.size)

    def my_print(self):
        '''Prints the square to the console.'''
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
