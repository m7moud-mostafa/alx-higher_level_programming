#!/usr/bin/python3
"""
This is an important module
"""


def write_file(filename="", text=""):
    """reads a file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    print(write_file("my_first_file.txt", "This School is so cool!\n"))
