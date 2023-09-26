#!/usr/bin/python3
"""Module for appending"""


def append_write(file_name="", text=""):
    """Appends to a file
    Parm file_name: name of file
    Param text: text to append
    """
    with open(file_name, "a", encoding="UTF8") as f:
        return f.write(text)
