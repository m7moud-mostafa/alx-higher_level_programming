#!/usr/bin/python3
"""This module contains the Mylist class"""


class MyList(list):
	"""A class that inherits the list class"""

	def print_sorted(self):
		"""prints the list sorted"""
		self.l = self.copy()
		self.l.sort()
		print(self.l)


my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
