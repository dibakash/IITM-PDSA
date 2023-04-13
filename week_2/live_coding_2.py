"""
Write a Python function findCommonElements(L1, L2) that accepts two integer lists L1 and L2
of same length n and return a list that contains elements that are common to both lists. Write a
efficient solution that runs in O(nlogn) time.

L1 contains all distinct integers and L2 contains all distinct integers, but there can be many
elements common between L1 and L2 .

Returned list contains all elements that are common to L1 and L2 . The elements in the
returned list can be in any order.

For example.
if L1 = [5, 8, 2] and L2 = [6, 8, 1] then, findCommonElements(L1, L2) should return list [8].
if L1 = [3, 7, 2, 9, 5] and L2 = [6, 3, 7, 5, 4] then, findCommonElements(L1, L2) should return list
[3, 7, 5]. Elements in returned list can be in any order.
"""


def binary_search(L, target):
    n = len(L)
    if n < 1:
        return False

    left = 0
    right = n - 1

    while left <= right:
        mid = left + (right - left) // 2

        if L[mid] == target:
            return True
        elif L[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def findCommonElements(L1, L2):
    L1.sort()
    L3 = []
    for item in L2:
        if binary_search(L1, item) == True:
            L3.append(item)
    return L3


if __name__ == "__main__":
    A = [23, 24, 18, 22, 20, 10, 17, 12, 16, 19, 21, 15, 14, 11, 13]
    B = [23, 22, 33, 24, 31, 21, 20, 26, 30, 29, 25, 27, 28, 34, 32]
    result = findCommonElements(A, B)
    result.sort()
    print(result)

    # answer should be = [20, 21, 22, 23, 24]
