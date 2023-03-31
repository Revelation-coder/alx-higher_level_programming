#!/usr/bin/python3
'''Module for easy multiplication function'''


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy

    Args:
    m_a: list of lists of integers/floats representing the first matrix
    m_b: list of lists of integers/floats representing the second matrix

    Returns:
    The product of the two matrices

    Raises:
    ValueError: If matrices can't be multiplied
    TypeError: If m_a or m_b is not a list of lists of integers/
    floats or is empty
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty and m_b can't be empty")
    if not all(isinstance(lst, list) for lst in m_a) or not all(isinstance(lst, list) for lst in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")
    if not all(isinstance(num, (int, float)) for lst in m_a for num in lst) or not all(isinstance(num, (int, float)) for lst in m_b for num in lst):
        raise TypeError("m_a should contain only integers or floats and m_b should contain only integers or floats")
    if not all(len(lst) == len(m_a[0]) for lst in m_a) or not all(len(lst) == len(m_b[0]) for lst in m_b):
        raise TypeError("each row of m_a must be of the same size and each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.dot(m_a, m_b)
