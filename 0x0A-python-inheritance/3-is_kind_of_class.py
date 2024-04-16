#!/usr/bin/python3
"""
This module contains many functions
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if it is an instance of a class that inherited from, the specified class.
    """
    return isinstance(obj, a_class)
