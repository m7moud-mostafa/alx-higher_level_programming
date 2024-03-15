#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0

    for row in matrix:
        j = 0
        for col in row:
            if j < len(row) - 1:
                print("{}".format(col), end=" ")
                j += 1
            else:
                print("{}".format(col), end="")
        print("")
        i += 1
