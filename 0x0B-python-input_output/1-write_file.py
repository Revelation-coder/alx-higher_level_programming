#!/usr/bin/python3
"""
This module contains a function that writes a given string to a file.

The function takes in a file name and a text string
Writes the string to the file.
If the file already exists, the function overwrites its contents.
Else the function creates the file.
The function returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    :param filename: The name of the file to write to.
    :type filename: str
    :param text: The text to write to the file.
    :type text: str
    :return: The number of characters written to the file.
    :rtype: int
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
