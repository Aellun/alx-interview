#!/usr/bin/python3
'''
Functions to rotate an n x n matrix 90 degrees clockwise.
'''


def transpose_matrix(matrix, n):
    '''
    Transpose the given n x n matrix in place.
    Args:
        matrix (List[List[int]]): The 2D matrix to be transposed.
        n (int):dimension of the Matrix
    '''
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    '''
    Reverse each row of the given n x n matrix in place.
    Args:
        matrix (List[List[int]]): The 2D matrix whose rows are to be reversed.
    '''
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    '''
    Rotate the given n x n matrix 90 degrees clockwise.
    Args:
        matrix (List[List[int]]): The 2D matrix to be rotated.
    '''
    n = len(matrix)

    # Transpose the matrix
    transpose_matrix(matrix, n)

    # Reverse each row
    reverse_matrix(matrix)
