#!/usr/bin/python3

"""5-base_geometry
A base geometry class.
"""


class BaseGeometry:
    """Geometry class with area method"""

    def area(self):
        """Area method that raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Methodi that validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
