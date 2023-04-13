# python week_2/algos/merge_sort.py

L = [11, 11, 7, 10, 15, 6, 4, 13, 11, 1, 6, 6, 4, 4, 10]
compare_ans = sorted(L)


def merge(left, right):
    l, r = len(left), len(right)
    res, i, j, k = [], 0, 0, 0

    while k < l + r:
        if i == l:  # left list is empty
            res.extend(right[j:])
            k += r - j
        elif j == r:  # right list is empty
            res.extend(left[i:])
            k += l - i
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
            k += 1
        else:
            res.append(right[j])
            j += 1
            k += 1

    return res


def merge_sort(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])

    return merge(left, right)


def merge_sort_v2(L):
    if len(L) <= 1:
        return L
    mid = len(L) // 2
    left = merge_sort_v2(L[:mid])
    right = merge_sort_v2(L[mid:])

    return merge_v2(left, right)


def merge_v2(left, right):
    l, r = len(left), len(right)
    res, i, j = [], 0, 0

    while i < l and j < r:
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res += left[i:]
    res += right[j:]

    return res


print(L)
# L = merge_sort(L)
L = merge_sort_v2(L)
print(L)
print("correct" if compare_ans == L else "wrong")
