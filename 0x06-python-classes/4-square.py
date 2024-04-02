#!/usr/bin/python3
"""
This module enhances the Square class by adding getter and setter for the
private instance attribute 'size' to control its access and validation.
"""


class Square:
    """
    A class that represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the Square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.
         """
        return self.__size * self.__size
