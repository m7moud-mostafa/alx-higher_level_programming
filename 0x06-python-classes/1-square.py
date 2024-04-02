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

    def __init__(self, size):
        """
        Initializes a new Square with a given size.

        Args:
        size (int): The size of a side of the square.
        """
        self.__size = size
