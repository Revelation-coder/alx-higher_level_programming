#!/usr/bin/python3
'''This module defines a function that divides a matrix'''


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and returns a new matrix.

    Args:
        matrix (list of list of int or float): The matrix to be divided.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list of list of float: The resulting matrix.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   or if each row of the matrix doesn't have the same size,
                   or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    # Check the matrix input
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Check the divisor input
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide the matrix elements
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix
