#!/usr/bin/python3
'''This module defines square  class'''


class Square:
    '''Initialize a square class'''
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        '''getter function'''
        return self._size

    @size.setter
    def size(self, value):
        '''Setter function '''
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        '''function to get area'''
        return self.size ** 2

    def __eq__(self, other):
        '''Function to compare area'''
        return self.area() == other.area()

    def __ne__(self, other):
        '''Function to compare area'''
        return self.area() != other.area()

    def __gt__(self, other):
        '''Function to compare area'''
        return self.area() > other.area()

    def __ge__(self, other):
        '''Function to compare area'''
        return self.area() >= other.area()

    def __lt__(self, other):
        '''Function to compare area'''
        return self.area() < other.area()

    def __le__(self, other):
        '''Function to compare area'''
        return self.area() <= other.area()
