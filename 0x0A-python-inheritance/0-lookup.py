#!/usr/bin/python3

"""Lookup: Function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """Returns list of attributes & methods"""
    return dir(obj)
