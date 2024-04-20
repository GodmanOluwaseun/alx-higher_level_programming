#!/usr/bin/python3

"""2-is_same_class:
Function that checks if object is an instance of specified class.

Returns:
    Returns True
    otherwise False.
"""


def is_same_class(obj, a_class):
    """Checks if obj is type a_class"""
    type_check = type(obj)
    if type_check == a_class:
        return True
    else:
        return False
