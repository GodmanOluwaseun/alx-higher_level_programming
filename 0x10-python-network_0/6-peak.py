#!/usr/bin/python3

"""
6-peak
    Function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Returns peak number"""

    arr = list_of_integers

    if len(arr) == 0:
        return None

    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]
        elif arr[mid + 1] > arr[mid]:
            start = mid + 1
        else:
            end = mid
    return arr[start]
