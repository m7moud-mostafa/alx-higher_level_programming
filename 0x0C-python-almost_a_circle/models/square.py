#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square attributes"""
        list_attrs = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, list_attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
