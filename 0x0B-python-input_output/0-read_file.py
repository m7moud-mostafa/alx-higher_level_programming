#!/usr/bin/python3
"""
This is an important module
"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")


if __name__ == "__main__":
    with open("my_first_file.txt", "r", encoding="utf-8") as f:
        print(f.readline(), end="")
        print(f.readline(), end="")
        print(f.readlines())
