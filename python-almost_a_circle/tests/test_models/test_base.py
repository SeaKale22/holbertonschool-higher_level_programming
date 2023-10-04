#!/usr/bin/python3
"""Test module for Base class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

class test_Base_to_json_str(unittest.TestCase):
    """Tests the to_json_string method"""
    def test_normal(self):
        """tests for correct useage"""
        r1 = Rectangle(10, 7, 2, 8, 77)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(json_dict, '[{"id": 77, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_wrong(self):
        """tests incorrect useage"""
        r1 = Rectangle(2, 2, 3, 4)
        json_dict = Base.to_json_string([])
        self.assertEqual(json_dict, "[]")
        with self.assertRaises(TypeError) as e:
            r2 = Rectangle(2, 2, 3, 3)
            json_dict2 = Base.to_json_string()
