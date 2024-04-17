#!/usr/bin/python3
"""
This module contains the solution for
the technical interview
"""


def pascal_triangle(n):
    """returns a lng the Pascal’s triangle of n"""
    if n <= 0:
        return []
    tri = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(tri[i - 1][j - 1] + tri[i - 1][j])
        row.append(1)
        tri.append(row)
    return tri
