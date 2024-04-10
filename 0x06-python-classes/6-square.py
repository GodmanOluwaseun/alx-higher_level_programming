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
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position[0], int) or \
                not isinstance(position[1], int):
                    raise TypeError("position must be a tuple of 2 \
                            positive integers")
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
        if not isinstance(value[0], int) or \
                not isinstance(value[1], int):
                    raise TypeError("position must be a tuple of 2 \
                            positive integers")
        self.__position = value

    def area(self):
        """Area returns current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout square with character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    if self.__position[1] > 0:
                        print("_", end="")
                    else:
                        print("#", end="")
                print()