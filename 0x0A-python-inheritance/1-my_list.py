#!/usr/bin/python3
"""This module contains the Mylist class"""


class MyList(list):
    """A class that inherits the list class"""

    def print_sorted(self):
        """prints the list sorted"""
        self.list_ = self.copy()
        self.list_.sort()
        print(self.list_)

my_list = MyList()
print(my_list)
my_list.print_sorted()
print(my_list)