#!/usr/bin/python3
"""
This module defines a Square class which allows querying and updating the size
of the Square.
"""


class Square:
    """
    A class to represent a square.
     """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the Square."""
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

    @property
    def position(self):
        """Retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position value"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            col, rows = self.__position
            for i in range(rows):
                print()
            for i in range(self.__size):
                print("{}{}".format(" " * col, "#" * self.__size))
