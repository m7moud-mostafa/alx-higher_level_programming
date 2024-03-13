#!/usr/bin/python3
for i in range(100):
    if i < 10:
        j = "0"
    else:
        j = ""

    if not (i == 99):
        print("{}{}".format(j, i), end=", ")
    else:
        print("{}{}".format(j, i))
