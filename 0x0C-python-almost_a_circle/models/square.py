#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the Square class"""
        super().__init__(size, size, x, y, id)
        self.size = self.height


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()
