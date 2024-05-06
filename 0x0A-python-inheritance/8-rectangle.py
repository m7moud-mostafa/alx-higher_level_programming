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
