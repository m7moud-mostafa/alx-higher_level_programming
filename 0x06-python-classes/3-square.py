#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute size.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
    size (int): The size of a side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square with a given size.

        Args:
        size (int): The size of a side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size
