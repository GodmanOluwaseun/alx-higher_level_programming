


#!/usr/bin/python3

"""
0-square
    This module containss a class Square
    that defines a square.

"""


class Square:
    """Class Square that defines a square of size:"""
    def __init__(self, size=0):
        try:
            if size >= 0:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
