#!/usr/bin/python3
"""
This module contains a function that appends a given string to a file.
The function takes in a file name and a text string
Appends the string to the end of the file.
If the file does not exist, the function creates it.
The function returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append the given text to the file with the given filename.
    :param filename: The name of the file to append to.
    :type filename: str
    :param text: The text to append to the file.
    :type text: str
    :return: The number of characters appended to the file.
    :rtype: int
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
