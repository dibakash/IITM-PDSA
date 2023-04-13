"""
Given a list L of random numbers and another number pairSum , find whether there exists two numbers in the list such that their sum is equal to pairSum .

Write a Python function findPair(L, pairSum) that return True if there exist a pair of integers in L whose sum is equal to x , False otherwise.. Try to write a solution which is O(nlogn) or better.

Hint: Try to sort the list first.
For example consider the list [10, 4, 11, 5, 1, 8, 7] . We need to find if there exists any pair whose sum is equal to 21. 11+10 = 21. So the function should return True.

For the same list if we want to find if there exist any pair whose sum is equal to 2. Clearly there is no such pair so the function should return False.
"""


def findPair(L, pairSum):
    memo = set()
    for num in L:
        if pairSum - num in memo:
            return True
        memo.add(num)
    return False


# Suffix code
L = [int(item) for item in input().split()]
pairsum = int(input())
print(findPair(L, pairsum))


# version 2
def findPair(L, x):
    L.sort()
    left = 0
    right = len(L) - 1

    while left < right:
        sum = L[left] + L[right]
    if sum == x:
        return True
    elif sum > x:
        right -= 1
    else:
        left += 1

    return False
