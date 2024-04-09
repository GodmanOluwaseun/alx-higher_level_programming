#!/usr/bin/python3
"""
0-square
    This module containss a class Square
    that defines a square.

"""


class Square:
    """Class Square that defines a square of size:"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
