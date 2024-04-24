#!/usr/bin/python3
"""This module contains the text_indentation function"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: `.`, `?` and `:`
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char = 0
    while char < len(text):
        if text[char] in ['.', '?', ':']:
            print(text[char])
            print("")
            if char + 1 < len(text) and text[char + 1] == ' ':
                char += 2
            else:
                char += 1
        else:
            print(text[char], end='')
            char += 1
