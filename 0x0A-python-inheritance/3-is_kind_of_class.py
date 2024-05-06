#!/usr/bin/python3
"""This module contains the is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is exactly
    an instance of the specified class
    """
    return isinstance(obj, a_class)


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
