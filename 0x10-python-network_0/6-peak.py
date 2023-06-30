#!/usr/bin/python3
"""
   function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Function to find a peak in a list of unsorted integers.
    Returns the peak element if found, None otherwise.
    """
    if not list_of_integers:
        return None

    start = 0
    end = len(list_of_integers) - 1

    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return list_of_integers[start]
