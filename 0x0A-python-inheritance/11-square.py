#!/usr/bin/python3

"""10-square:
Class Square that inherits from Rectangle 9-rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Square area method"""
        return self.__size * self.__size

    def __str__(self):
        """Str method"""
        width = str(self.__size)
        height = str(self.__size)
        string = f"[Square] {width}/{height}"
        return string
