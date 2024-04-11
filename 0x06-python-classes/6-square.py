#!/usr/bin/python3

"""6-square: This module contains a class Square that defines a square.

Attributes:
    size (int): Determines length of the square sides, must be +ve int.
    Position (tupple): Tuple of 2 integers setting the coordinates,
    it is a +ve int.

Class:
    Square: Defines a square object with a given size and position.

Getters:
    size gets and returns the size attribute.
    position  returns position attribute

Setters:
    size.setter sets the value of the size attribute, takes +ve int.
    position.setter sets value of position, takes tuple of 2 +ve ints.

Methods:
    area: Calculates and returns the area of the square.
    my_print: Prints the square with '#' characters to stdout,
    using position.
"""


class Square:
    """Class Square that defines a square of size
    Args:
        arg1 (int): size
        arg2 (tuple): position
    Attributes:
        size (int): length of square
        position  (tuple): Position to start print from.
    Functions:
        __init__(self, size=0, position=(0, 0))
        area(self)
        my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square object

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if len(position) != 2 or not isinstance(position[0], int) or \
                not isinstance(position[1], int) or \
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """Returns Position atribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position attribute"""
        if len(value) != 2 or not isinstance(value[0], int) or \
                not isinstance(value[1], int) or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area returns current square area.

        Returns:
            The return value. area of square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout square with character #

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
