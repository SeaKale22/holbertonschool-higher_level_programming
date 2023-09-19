#!/usr/bin/python3
"""Module for matrix division"""


def matrix_divided(matrix, div):
    """Divides a matrix:
    param matrix: must be a list of lists of integers or floats
    param div: must be a number (integer or float)
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
    first_row_size = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row]
                  for row in matrix]
    return new_matrix
