#!/usr/bin/python3
'''This module defines square  class'''
class Square:
    '''Initialize a square class'''
    def __init__(self, size=0, position=(0, 0)):
        '''function to initialize square size'''
	self.size = size
        self.position = position

    @property
    def size(self):
        '''getter function'''
        return self._size

    @size.setter
    def size(self, value):
        '''Setter function '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        '''function to initialize position'''
        return self._position

    @position.setter
    def position(self, value):
        '''function to set position'''
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        '''function to get area'''
        return self.size ** 2

    def my_print(self):
        '''Function to print the square'''
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

