#!/usr/bin/python3
"""Module defining add_attribute method"""


def add_attribute(*args):
    """function  to add attribute
    else raises type error
    """
    if "main" in str(type(args[0])):
        setattr(args[0], args[1], args[2])
    else:
        raise TypeError("can't add new attribute")
