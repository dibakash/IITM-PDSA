# python week_2/algos/merge_sort.py

L = [11, 11, 7, 10, 15, 6, 4, 13, 11, 1, 6, 6, 4, 4, 10]
compare_ans = sorted(L)


def merge(left, right):
    left_len, right_len = len(left), len(right)
    i, j = 0, 0
    res, k = [], 0

    while k < left_len + right_len:
        if i == left_len:  # left list is empty
            res.extend(right[j:])
            k += right_len - j

        elif j == right_len:  # right list is empty
            res.extend(left[i:])
            k += left_len - i

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


print(L)
L = merge_sort(L)
print(L)
print("correct" if compare_ans == L else "wrong")
