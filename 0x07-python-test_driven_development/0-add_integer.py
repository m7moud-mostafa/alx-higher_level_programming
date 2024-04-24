#!/usr/bin/python3
"""This module contains add_integer function"""


def add_integer(a, b=98):
    """adds to integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
        
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
