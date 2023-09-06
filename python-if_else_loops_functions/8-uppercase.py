#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - 32)
            upper_str += upper_char
        else:
            upper_str += char
    print("{}".format(upper_str))
