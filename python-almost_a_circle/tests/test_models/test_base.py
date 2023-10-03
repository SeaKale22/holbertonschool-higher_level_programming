#!/usr/bin/python3
"""Test module for Base class"""

import unittest
from models.base import Base


class test_Base(unittest.TestCase):
    """tests the Base Class"""
    def test_init(self):
        """test basic init with no params"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)

    def test_init_param(self):
        """test for when having a param"""
        b1 = Base(22)
        self.assertEqual(b1.id, 22)
        b2 = Base(45)
        self.assertEqual(b2.id, 45)
