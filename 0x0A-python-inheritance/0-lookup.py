#!/usr/bin/python3


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    
    Args:
        obj: The object to inspect.
  
    Returns:
    A list of strings representing the available attributes and methods of the object.
    """
    return [attr for attr in dir(obj) 
    if not callable(getattr(obj, attr)) 
    or not attr.startswith("__")]
