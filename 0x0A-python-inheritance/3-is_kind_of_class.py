#!/usr/bin/python3

"""3-is_kind_of_class:
Function that checks if a class inherited from another class.

Return value:
    returns true or false.
"""

def is_kind_of_class(obj, a_class):
    """Checks if obj is a subclass of a_class"""
    obj_class = type(obj)
    if isinstance(a_class, obj_class) or issubclass(a_class, obj_class):
        return True
    else:
        return False
