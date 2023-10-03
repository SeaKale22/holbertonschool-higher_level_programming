#!/usr/bin/python3
"""tests for square"""

import unittest
from models.square import Square


class test_Square(unittest.TestCase):
    """tests square"""
    def test_init(self):
        """test normal init"""
        s1 = Square(2)
        self.assertEqual(s1.size, 2)
        s2 = Square(2, 3, 4)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)
    def test_init_error(self):
        """tests passing bad param to Square"""
        with self.assertRaises(TypeError) as e:
            s1 = Square("string")
        with self.assertRaises(ValueError) as e:
            s2 = Square(0)
        with self.assertRaises(ValueError) as e:
            s3 = Square(3, -1, 4)
