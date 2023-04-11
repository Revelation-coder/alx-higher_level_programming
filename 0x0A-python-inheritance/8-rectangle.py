#!/usr/bin/python3
"""Module defining BaseGeometry class"""


class BaseGeometry:
    """A class defining basic geometry properties"""
    def area(self):
        """Raises an exception with message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if value is an integer greater than 0,
        else raises an exception

        Args:
            name (str): name of value
            value (int): value to be validated

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0". format(name))


class Rectangle(BaseGeometry):
    """A class defining Rectangle properties"""
    def __init__(self, width, height):
        """Function to initialize Rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
