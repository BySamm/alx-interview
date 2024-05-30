#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an n by n 2D matrix in place.
    """
    if not isinstance(matrix, list):
        return
    if len(matrix) == 0:
        return
    if not all(isinstance(row, list) for row in matrix):
        return
    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        return

    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # offset is used to avoid overwriting
            offset = i - first
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
