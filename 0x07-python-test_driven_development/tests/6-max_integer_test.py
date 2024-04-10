#!/usr/bin/python3
"""
Unittest for max_integer([..]).
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This class contains unittests for the max_integer function.
    """

    def test_max_integer(self):
        """Test method for max integer in a list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([-2, -4, -6, -8]), -2)

    def test_type_errors(self):
        """Test method for type errors."""
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer(10)
        with self.assertRaises(TypeError):
            max_integer("string")

if __name__ == '__main__':
    unittest.main()
