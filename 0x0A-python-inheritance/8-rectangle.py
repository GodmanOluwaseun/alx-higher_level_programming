#!/usr/bin/python3

"""8-base_geometry
A base geometry, and rectangle class.
"""

"""
class BaseGeometry:
    Geometry class

    def area(self):
        ""/"Area method that raises exception"/""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ""/"Methodi that validates value"/""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class that inherits BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
