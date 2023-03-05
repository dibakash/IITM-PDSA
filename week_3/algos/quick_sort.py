# python week_2/algos/quick_sort.py

L = [11, 11, 7, 10, 15, 6, 4, 13, 11, 1, 6, 6, 4, 4, 10]

compare_result = sorted(L)


def quick_sort(L, l, r):
    if r - l <= 1:
        return L
    pivot, lower, upper = L[l], l + 1, l + 1
    for i in range(l + 1, r):
        if L[i] > pivot:  # extend upper segment
            upper += 1
        else:  # exchange L[i] with start of upper segment
            L[i], L[lower] = L[lower], L[i]
            # shift both segments
            lower, upper = lower + 1, upper + 1
    # move the pivot between lower and upper
    L[l], L[lower - 1] = L[lower - 1], L[l]
    # prepare new segment boundaries
    lower = lower - 1
    # sort left
    quick_sort(L, l, lower)
    # sort right
    quick_sort(L, lower + 1, upper)
    return L


print(L)
quick_sort(L, 0, len(L))
print(L)
print("correct" if compare_result == L else "wrong")
