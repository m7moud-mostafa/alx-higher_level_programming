#!/usr/bin/python3
"""This module contains the Rectangle class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """This class for Rectangle shape"""

    def __init__(self, width, height):
        """Initializing the class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a description of an object"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
