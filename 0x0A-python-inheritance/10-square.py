#!/usr/bin/python3
"""This module contains the Square class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
	"""Square Class"""

	def __init__(self, size):
		"""Initializing the Square class"""
		super().__init__(size, size)


if __name__ == "__main__":
	s = Square(13)

	print(s)
	print(s.area())
