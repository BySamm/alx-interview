#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle of height n.
    Pascal's triangle is a mathematical array of binomial
    coefficients arranged in a
    triangular form. Each number is the sum of the two directly
    above it in the previous row.
    Parameters:
    - n (int): The number of levels in Pascal's triangle to generate.
    Returns:
    - list of lists: A list where each sublist represents a level
    in Pascal's triangle => If n <= 0, returns an empty
    The function starts with a base check for non-positive values of n,
    where it returns an empty list.
    For positive n, it constructs the triangle level by level.
    Each level's entries are calculated
    by adding up appropriate pairs from the previous level.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
