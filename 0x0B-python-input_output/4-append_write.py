#!/usr/bin/python3
"""
function that appends a string at the end of a text file (UTF8)
returns the number of characters added
"""

def append_write(filename="", text=""):
    """Function to append text to a file"""
    with open(filename, 'a') as f:
        return f.write(text)
