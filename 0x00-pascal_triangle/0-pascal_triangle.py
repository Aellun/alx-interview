#!/usr/bin/python3
"""A script to determine Pascal's triangle for any number"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    triangle = []

    """Return an empty list if n is less than or equal to 0"""
    if n <= 0:
        return triangle
    """Generate each row of the triangle"""
    for i in range(n):
        temp_list = []
        """Each element is the sum of the two elements above it"""
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        """Append the row to the triangle"""
        triangle.append(temp_list)
    return triangle
