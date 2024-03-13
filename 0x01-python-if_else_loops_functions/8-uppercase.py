#!/usr/bin/python3

def uppercase(str):

    uppered_string = ""

    for char in str:
        if ord(char) in range(ord('a'), ord('z') + 1):
            uppered_string += chr(ord(char) - 32)
        else:
            uppered_string += char
    print("{}".format(uppered_string))
