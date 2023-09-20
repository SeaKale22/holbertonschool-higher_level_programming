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

    def test_max_beggining(self):
        """tests for max int at beginning of list"""
        result = max_integer([4, 1, 2, 3])
        self.assertEqual(result, 4)

    def test_max_end(self):
        """tests for max int at end of list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_one_neg_num(self):
        """tests for a single negitive number in list"""
        result = max_integer([2, 3, -6, 4])
        self.assertEqual(result, 4)

    def test_only_neg_nums(self):
        """tests for list of only negitive numbers"""
        result = max_integer([-3, -1, -2, -4])
        self.assertEqual(result, -1)

    def test_one_element(self):
        """tests for list of one element"""
        result = max_integer([1])
        self.assertEqual(result, 1)

    def test_empty_list(self):
        """tests for empty list"""
        result = max_integer([])

