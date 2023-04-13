"""
Merging two sorted array in place.

Given a custom implementation of list named MyList. On MyList objects you can perform read operations similar to the in-built lists in Python, example use A[i] to read element at index i in MyList object A. The only possible operation that you can use to edit data in MyList objects is by calling the swap method. For instance, A.swap(indexA, B, indexB) will swap values at A[indexA] and B[indexB] and A.swap(index1, A, index2) will swap values at A[index1] and A[index2], where indexA, indexB, index1, index2 are all integers.

Complete the Python function mergeInPlace(A, B) that accepts two MyLists A and B containing integers that are sorted in ascending order and merges them in place (without using any other list) such that after merging, A and B are still sorted in ascending order with the smallest element of both MyLists as the first element of A

Sample input
2 4 6 9 13 15
1 3 5 10
Sample output:
[1, 2, 3, 4, 5, 6]
[9, 10, 13, 15]

"""

#python
def mergeInPlace(A, B):
  m = len(A)
  n = len(B)
  if (m < 1 or n < 1):
    return

  # Find the smaller list of A and B.
  for i in range(0, m):
    # A and B are already sorted. B[0] will always be least in B,
    # as we will maintain its sortedness .
    if (A[i] > B[0]):
      A.swap(i, B, 0)

      # move `B[0]` to its correct position in B to maintain the sortedness of B
      j = 0
      while(j < n - 1 and B[j] > B[j + 1]):
        B.swap(j+1, B, j)
        j += 1
