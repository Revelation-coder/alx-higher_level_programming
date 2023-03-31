#!/usr/bin/python3
''' This module defines a function to add integers'''


def add_integer(a, b=98):
    """
    Returns the sum of two integers.

    :param a: an integer or float
    :param b: an integer or float (default: 98)
    :raises TypeError: if a or b are not integers or floats
    :return: an integer representing the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
