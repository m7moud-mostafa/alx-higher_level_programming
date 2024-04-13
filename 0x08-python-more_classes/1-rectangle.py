#!/usr/bin/python3

"""
this module will contain the Rectangle class
"""


class Rectangle:
    """
    this class does nothing
    """

    def __init__(self, width=0, hight=0):
        """Initialize the Class"""
        self.width = width
        self.hight = hight

    @property
    def width(self):
        """Retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def hight(self):
        """Retrieves hight"""
        return self.__hight

    @hight.setter
    def hight(self, value):
        """Sets hight"""
        if not isinstance(value, int):
            raise TypeError("hight must be an integer")
        if value < 0:
            raise ValueError("hight must be >= 0")
        self.__hight = value
