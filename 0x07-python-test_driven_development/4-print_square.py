#!/usr/bin/python3
"""This module contains the print_square function"""


def print_square(size):
    """prints a square with size = size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
