#!/usr/bin/python3
"""Module for read file"""


def read_file(file_name=""):
    """Reads a file
    Param file_name: the file to read from
    """
    with open(file_name, encoding="UTF8") as f:
        content = f.read()
        print(content)
