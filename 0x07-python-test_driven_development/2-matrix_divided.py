#!/usr/bin/python3
"""
A module that contains the matrix_divided function
"""


def matrix_divided(matrix, div):
    """Returns a new matrix divided by div"""
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not all(isinstance(elm, (int, float)) for row in matrix for elm in row):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        n_row = []
        for elem in row:
            n_row.append(round(elem / div, 2))
        new_matrix.append(n_row)
    return new_matrix
