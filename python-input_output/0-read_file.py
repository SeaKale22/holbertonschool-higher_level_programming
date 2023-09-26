#!/usr/bin/python3
"""Module for read file"""


def read_file(file_name=""):
    """Reads a file
    Param file_name: the file to read from
    """
    with open(file_name, "r") as f:
        for line in f:
            print(line)
