#!/usr/bin/python3
"""
This module contains many functions
"""


class MyList(list):
    """
    MyList that inherits from list and can print sorted list.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
