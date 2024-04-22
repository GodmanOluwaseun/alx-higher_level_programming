#!/usr/bin/python3

"""9-base_geometry
A base geometry, and rectangle class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Str method"""
        width = str(self.__width)
        height = str(self.__height)
        string = f"[Rectangle] {width}/{height}"
        return string
