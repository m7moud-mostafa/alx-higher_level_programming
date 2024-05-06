#!/usr/bin/python3
"""This module contains the Mylist class"""


class MyList(list):
    """A class that inherits the list class"""

    def print_sorted(self):
        """prints the list sorted"""
        self.l = self.copy()
        self.l.sort()
        print(self.l)
