## Live Coding Problem 3

"""
Write a function shuffle(l1,l2) that takes two lists, `l1` and `l2` as input, and returns a list consisting of the first element in `l1`, then the first element in `l2`, then the second element in `l1`, then the second element in `l2`, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

Sample Input

[0,2,4]
[1,3,5]

Output

python
[0, 1, 2, 3, 4, 5]
"""


def shuffle(l1, l2):
    left_len, right_len = len(l1), len(l2)
    i, j = 0, 0
    res, k = [], 0

    while k < left_len + right_len:
        if left_len == i:
            res.extend(l2[j:])
            k += right_len - j
        elif right_len == j:
            res.extend(l1[i:])
            k += left_len - i
        elif l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
            k += 1
        else:
            res.append(l2[j])
            j += 1
            k += 1
    return res


if __name__ == "__main__":
    #  suffix Code
    L1 = eval(input())
    L2 = eval(input())
    print(shuffle(L1, L2))
