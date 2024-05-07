#!/usr/bin/python3
"""This module contains the rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def __integer_validator(name, value, equalZero=False):
        """Validates if the value is not integer or less then 0"""
        if not isinstance(value, (int)):
            raise TypeError("{} must be an integer".format(name))

        if equalZero:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for width"""
        self.__integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height"""
        self.__integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for the x"""
        self.__integer_validator("x", value, True)
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the y"""
        self.__integer_validator("y", value, True)
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.height * self.width

    def display(self):
        """prints the rectangle"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """returns a description """
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                 self.id, self.x, self.y,
                                                 self.width, self.height))

    def update(self, *args):
        """updates the attributes"""
        length = len(args)
        if length >= 1:
            self.id = args[0]
        if length >= 2:
            self.width = args[1]
        if length >= 3:
            self.height = args[2]
        if length >= 4:
            self.x = args[3]
        if length >= 5:
            self.y = args[4]


if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)
