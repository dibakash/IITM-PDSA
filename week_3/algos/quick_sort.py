# python week_2/algos/quick_sort.py


def quick_sort(L, l, r):
    """
    The quick_sort function takes an array L and two indices l and r that define the range of the subarray/slice to sort.
    """
    # If the range of the subarray is less than or equal to 1, the function returns the subarray since it is already sorted (as only one element).
    if r - l <= 1:
        return L

    # Otherwise, the function selects the first element (pivot) as the pivot element and initializes two pointers: lower and upper both starting at l + 1.
    pivot, lower, upper = L[l], l + 1, l + 1

    # The function then iterates over the subarray elements from (l + 1) to r ("yet-to-be-seen" region). 
    # If an element is greater than the pivot element value, the upper pointer is incremented (to expand the region containing upper elements). 
    # If an element is less than or equal to the pivot, 
    # the element is exchanged with the first element of the "upper region" and both pointers are incremented.
    for i in range(l + 1, r):
        if L[i] > pivot:  # extend upper segment
            upper += 1
        else:  # exchange L[i] with start of upper segment
            L[i], L[lower] = L[lower], L[i]
            # shift both segments
            lower, upper = lower + 1, upper + 1

    # After the loop completes, the function exchanges the pivot element with the element at lower - 1.

    # move the pivot between lower and upper
    L[l], L[lower - 1] = L[lower - 1], L[l]
    # This ensures that all elements to the left till lower - 1 are less than or equal to the pivot, 
    # and all elements to the right from lower + 1 are greater than the pivot.

    # The function then recursively calls quick_sort on the subarray to the left of the pivot (from l to lower - 1) 
    # and the subarray to the right of the pivot (from lower to upper). 
    # This process continues until all subarrays have lengths 0 or 1, and the entire array is sorted.

    # prepare new segment boundaries
    lower = lower - 1
    # sort left
    quick_sort(L, l, lower)
    # sort right
    quick_sort(L, lower+1, upper)

    # Finally, the function returns the sorted subarray.
    return L


L = [11, 11, 7, 10, 15, 6, 4, 13, 11, 1, 6, 6, 4, 4, 10]

compare_result = sorted(L)

print(L)
quick_sort(L, 0, len(L))
print(L)
print("correct" if compare_result == L else "wrong")
