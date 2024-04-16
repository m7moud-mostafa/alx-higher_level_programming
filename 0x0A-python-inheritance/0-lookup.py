#!/usr/bin/python3
"""
This module contains the lookup class
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
