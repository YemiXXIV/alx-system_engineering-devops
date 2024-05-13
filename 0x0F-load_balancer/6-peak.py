#!/usr/bin/python3
"""
This finds the pick in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    function to find a peak in a list of unsorted integers
    """

    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1
    while left < right:
        middle = (left + right) // 2
        if list_of_integers[middle] < list_of_integers[middle + 1]:
            left = middle + 1
        else:
            right = middle
    return list_of_integers[left]
