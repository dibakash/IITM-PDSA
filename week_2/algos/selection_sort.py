# python week_2/algos/selection_sort.py

L = [11, 11, 7, 10, 15, 6, 4, 13, 11, 1, 6, 6, 4, 4, 10]
compare_ans = sorted(L)


def selection_sort(L):
    n = len(L)
    if n <= 1:
        return

    for i in range(n - 1):
        min_index = i
        if L[i + 1] < L[i]:
            for j in range(i + 1, n):
                if L[j] < L[min_index]:
                    min_index = j

            L[i], L[min_index] = L[min_index], L[i]


print(L)
selection_sort(L)
print(L)

print("correct" if compare_ans == L else "wrong")
