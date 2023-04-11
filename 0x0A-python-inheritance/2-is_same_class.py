#!/usr/bin/python3
'''
this module defines a function to check whther an object
is exactly an instance of the specified class
'''


def is_same_class(obj, a_class):
    """
    function: is_same_class
    obj: an object
    a_class: a class
    Returns: Bool
    """
    return type(obj) == a_class
