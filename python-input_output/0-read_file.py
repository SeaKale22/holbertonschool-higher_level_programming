#!/usr/bin/python3
"""Module for read file"""


def read_file(file_name=""):
    with open(file_name, "r") as f:
        for line in f:
            print(line)
