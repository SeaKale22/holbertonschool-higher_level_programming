#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer_tests"""
    def test_normal(self):
        """tests a normal integer matrix"""
        test_list = [1, 2, 4, 3]
        result = max_integer(test_list)
        self.assertEqual(result, 4)
