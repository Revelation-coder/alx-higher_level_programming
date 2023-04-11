#!/usr/bin/python3
"""This module defines class MyInt(int)"""


class MyInt(int):
    """A class defining MyInt properties"""
    def __init__(self, value):
        """INITIALISE CLASS"""
        self.num = value

    def __eq__(self, other):
        """CHECKS IF EQUAL"""
        return self.num != other

    def __ne__(self, other):
        """CHECKS IF NOT EQUAL"""
        return self.num == other
