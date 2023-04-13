"""
Write a function Findpeak(L) that accepts a list L of n distinct elements and returns the peak
element of the list. A list element is a peak if it is greater than its neighbors. For corner elements,
we need to consider only one neighbor. Write a solution of O(logn) complexity. Consider that
there is only one peak is in the list, L.
"""


def Findpeak(L):
    n = len(L)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        # Check Corners
        if mid == 0 and L[mid] > L[mid + 1]:
            return L[mid]
        elif mid == n - 1 and L[mid] > L[mid - 1]:
            return L[mid]

        # Check middle parts
        elif L[mid - 1] < L[mid] > L[mid + 1]:
            return L[mid]

        # Update high low
        elif L[mid - 1] > L[mid]:
            high = mid - 1
        else:
            low = mid + 1
