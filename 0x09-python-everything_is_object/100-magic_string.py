#!/usr/bin/python3
''' This module defines a function which returns n times string'''


def magic_string():
    '''magic string function no arguments'''
    magic_string.counter = getattr(magic_string, "counter", 0) + 1
    return ", ".join(["Holberton" for i in range(magic_string.counter)])
