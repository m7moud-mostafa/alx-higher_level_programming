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
            i = 1
            while char + i < len(text) and text[char + i] == ' ':
                i += 1
            char += i
        else:
            print(text[char], end='')
            char += 1


if __name__ == "__main__":
    text_indentation("Holberton. School? How are you:    John")
