#!/usr/bin/python3
"""module to print text"""


def text_indentation(text):
    """prints the text according to a format"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    in_sentence = False
    for char in text:
        if char in ('.', '?', ':'):
            result += char + '\n\n'
            in_sentence = False
        elif char != ' ':
            result += char
            in_sentence = True
        elif in_sentence:
            result += char

    lines = [line.strip() for line in result.split('\n')]
    formatted_text = '\n'.join(lines)
    print(formatted_text, end='')
