# python week_2/algos/insertion_sort.py

L = [11, 11, 7, 10, 15, 6, 4, 13, 11, 1, 6, 6, 4, 4, 10]
compare_ans = sorted(L)


def insertion_sort(L):
    n = len(L)
    if n <= 1:
        return

    for i in range(1, n):
        j = i
        while L[j] < L[j - 1] and j > 0:
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= 1


# def insertion_sort(L):
#     n = len(L)
#     if n <= 1:
#         return

#     for i in range(1, n):
#         key = L[i]
#         j = i
#         while key < L[j - 1] and j > 0:
#             L[j] = L[j - 1]
#             j -= 1
#         L[j] = key


print(L)
insertion_sort(L)
print(L)
print("correct" if compare_ans == L else "wrong")
