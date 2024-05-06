#!/usr/bin/python3
"""This module contains the Square class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initializing the Square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Returns a description about the object"""
        return "[Square] {}/{}".format(self.__size, self.__size)


if __name__ == "__main__":

    s = Square(13)

    print(s)
    print(s.area())
