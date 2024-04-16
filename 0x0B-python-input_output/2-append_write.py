#!/usr/bin/python3
"""
This is an important module
"""


def append_write(filename="", text=""):
    """reads a file"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    print(append_write("my_first_file.txt", "This School is so cool!\n"))
