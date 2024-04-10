#!/usr/bin/python3
"""
0-square
    This module containss a class Square
    that defines a square.

Method:
    area Calculates and returns area of square.
"""


class Square:
    """Class Square that defines a square of size:"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area returns current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout square with character #"""
        for i in range(__size):
            for j in range(__size):
                print("#", end="")
            print()
