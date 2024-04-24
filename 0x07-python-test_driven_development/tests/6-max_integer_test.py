#!/usr/bin/python3
"""This is the file to test the max_integer function"""


import unittest

max_integer = __import__("6-max_integer").max_integer

class MaxIntegerTest(unittest.TestCase):
    """
    The unittest class to test the max_integer function
    """

    def test_values(self):
        """tests the value from the max_integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([-2, -4, -6, -8]), -2)

    def test_types(self):
        """tests for types errors"""
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer(10)
        with self.assertRaises(TypeError):
            max_integer([5, 5, 3, "mahmoud"])
