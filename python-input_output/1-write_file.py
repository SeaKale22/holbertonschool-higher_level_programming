#!/usr/bin/python3
"""Module for write file"""


def write_file(file_name="", text=""):
    with open(file_name, "w", encoding="UTF8") as f:
        return f.write(text)