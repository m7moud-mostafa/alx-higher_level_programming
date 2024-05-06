#!/usr/bin/python3
"""This module contains the Mylist class"""


class MyList(list):
    """A class that inherits the list class"""

    def print_sorted(self):
        """prints the list sorted"""
        self.list_ = self.copy()
        self.list_.sort()
        print(self.list_)


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(-49)
    my_list.append(5)
    my_list.append(-4)
    my_list.append(4)
    my_list.append(50)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
