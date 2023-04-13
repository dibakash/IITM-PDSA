# python week_2/grpa1.py
"""
Write a python function combinationSort(strList) that takes a list of unique strings strList as an argument, where each string is a combination of a letter from a to z and a number from 0 to 99, the initial character in string being the letter. For example a23, d5, q99 are some strings in this format. This function should sort the list and return two lists (l1, l2) in the order mentioned below.

L1: First list should contain all strings sorted in ascending order with respect to the first character only. All strings with same initial character should be in the same order as in the original list.

L2: In the list L1 above, sort the strings starting with same character, in descending order with respect to the number formed by the remaining characters.

Example
Sample input 1:
L : d34, g54, d12, b87, g1, c65, g40, g5, d77

sample output 1:
L1: b87, c65, d34, d12, d77, g54, g1, g40, g5
L2: b87, c65, d77, d34, d12, g54, g40, g5, g1

L = ["d34", "g54", "d12", "b87", "g1", "c65", "g40", "g5", "d77"]
"""


def get_char_num(char_num):
    return char_num[0], int(char_num[1:])


def merge_sort(L, style):
    n = len(L)
    if n <= 1:
        return L
    mid = n // 2

    left_L = merge_sort(L[:mid], style)
    right_L = merge_sort(L[mid:], style)

    res = merge(left_L, right_L, style)
    return res


def merge(left_L, right_L, style):
    left_len, right_len = len(left_L), len(right_L)
    i, j = 0, 0
    res, k = [], 0

    while k < left_len + right_len:
        if left_len == i:
            if style == "desc":
                res.extend(merge_sort(right_L[j:], style))
            else:
                res.extend(right_L[j:])
            k += right_len - j
        elif right_len == j:
            if style == "desc":
                res.extend(merge_sort(left_L[i:], style))
            else:
                res.extend(left_L[i:])
            k += left_len - i
        else:
            # compare char and digits
            c_left, n_left = get_char_num(left_L[i])
            c_right, n_right = get_char_num(right_L[j])

            if c_left < c_right:
                res.append(left_L[i])
                i += 1
                k += 1
            elif c_left > c_right:
                res.append(right_L[j])
                j += 1
                k += 1
            else:
                if style == "desc" and n_left <= n_right:
                    res.append(right_L[j])
                    j += 1
                    k += 1
                else:
                    res.append(left_L[i])
                    i += 1
                    k += 1

    return res


def combinationSort(strList):
    L = list(s.replace(" ", "") for s in strList.split(","))
    print(L)
    res1 = merge_sort(L, "default")
    res2 = merge_sort(L, "desc")

    r1s = "L1:"
    r2s = "L2:"

    for i in range(len(L)):
        if i != len(L) - 1:
            r1s += f" {res1[i]},"
            r2s += f" {res2[i]},"
        else:
            r1s += f" {res1[i]}"
            r2s += f" {res2[i]}"

    return f"{r1s}\n{r2s}"


if __name__ == "__main__":
    s = "d34, g54, d12, b87, g1, c65, g40, g5, d77"
    results = combinationSort(s)

    print(results)
