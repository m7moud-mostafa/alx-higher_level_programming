#!/usr/bin/python3
"""
This is an important module
"""

def read_file(filename=""):
    """reads a file"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

if __name__ == "__main__":
    read_file("README.md")