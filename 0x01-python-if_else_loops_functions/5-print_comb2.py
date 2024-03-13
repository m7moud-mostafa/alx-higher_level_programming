#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if not (i == j == 9):
            print("{}{}".format(i, j), end=", ")
        else:
            print("{}{}".format(i, j))
