#!/usr/bin/python3
"""tests Rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Rectangle(unittest.TestCase):
    """tests the Rectangle class"""
    def test_init(self):
        """tests normal initilization"""
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        r2 = Rectangle(2, 3, 4, 5)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 5)
    
    def test_init_param_err(self):
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle("string", 2)
        with self.assertRaises(ValueError) as e:
            r2 = Rectangle(3, 0)
        with self.assertRaises(ValueError) as e:
            r3 = Rectangle(2, 3, -4, 5)