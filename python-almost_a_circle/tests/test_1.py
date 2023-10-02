#!/usr/bin/python3
"""Test module for task 1"""

import unittest
from models.base import Base

def test_no_arg():
    """tests for no param to base"""
    b = Base()
    print(b.id)

def test_int_arg():
    """tests for int param to base"""
    b = Base(23)
    print(b)

def test_str_arg():
    """tests for st param to base"""
    b = Base("string")
    print(b)
