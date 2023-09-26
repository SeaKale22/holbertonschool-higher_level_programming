#!/usr/bin/python3
"""Module for write file"""


def write_file(file_name="", text=""):
    """Writes a text file
    Param file_name: the name of the file to write
    Param text: text to write into file
    Returns: Number of characters written
    """
    with open(file_name, "w", encoding="UTF8") as f:
        return f.write(text)