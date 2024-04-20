#!/usr/bin/python3

"""4-inherits_from:
Function that checks if an object is a instance of a class that
inherits from the given class.

Returns:
    Returns true of false.
"""


def inherits_from(obj, a_class):
    """Checks if obj is instance of a class that inherits a_class"""
    obj_class = type(obj)
    if obj_class is a_class:
        return False
    else:
        return issubclass(obj_class, a_class)
