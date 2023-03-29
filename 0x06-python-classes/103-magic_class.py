#!/usr/bin/python3
'''This module defines class MagicClass wc reverses given class to bytecode'''
import math


class MagicClass:
    ''' Magic Class reverses given Class to bytecode'''

    def __init__(self, radius=0):
        '''Function to initialize radius'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''function to get area'''
        return self.__radius**2 * math.pi

    def circumference(self):
        '''function to get circumferrence'''
        return 2 * math.pi * self.__radius
