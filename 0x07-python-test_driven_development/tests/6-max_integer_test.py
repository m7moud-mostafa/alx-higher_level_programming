#!/usr/bin/python3
"""This is the file to test the max_integer function"""


import unittest

max_integer = __import__("6-max_integer").max_integer

class Max_integer_testing(unittest.TestCase):
	"""
	The unittest class to test the max_integer function
	"""
	def Value_test(self):
		"""tests the value from the max_integer"""
		self.assertEqual(max_integer([4, 15, 3, 6, 6, 3]), 15)

	def type_test(self):
		"""tests for types errors"""
		self.assertRaises(max_integer(5), TypeError)
		self.assertRaises(max_integer([4, 5, 6, 6, "mahmoud"]), TypeError)
