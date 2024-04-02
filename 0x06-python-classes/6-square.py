#!/usr/bin/python3
"""
This module defines a Square class which allows querying and updating the size
and position of the Square, calculating its area, and printing the Square using
the '#' character, with the position offset.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
    __size (int): The size of a side of the square.
    __position (tuple): The position of the square as coordinates (x, y).

    Methods:
    area(): Returns the area of the square.
    my_print(): Prints the square using the '#' character, offset by position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square.

        Args:
        size (int): The size of the square.
        position (tuple): The position of the square as (x, y).
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

        Args:
        value (int): The new size of the square.

        Raises:
        TypeError: If `value` is not an integer.
        ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the Square.

        Args:
        value (tuple): The new position of the square as (x, y).

        Raises:
        TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#' to stdout, offset by position.
        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            # Print the new lines for the vertical offset
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                # Print the spaces for the horizontal offset
                print(" " * self.__position[0], end="")
                # Print the '#' characters for the square
                print("#" * self.__size)
