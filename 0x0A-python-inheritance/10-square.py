#!/usr/bin/python3
from 9-rectangle import Rectangle

class Square(Rectangle):
    """
    Class Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Instantiates with size. Size must be a positive integer, validated by integer_validator.
        """
        super().__init__(size, size)  # Size passed as both width and height
    
    def area(self):
        """
        Returns the area of the square.
        """
        return self._Rectangle__width * self._Rectangle__height
