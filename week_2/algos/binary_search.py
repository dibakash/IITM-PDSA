# binary search
# python week_2/algos/binary_search.py

Main_L = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 19, 29, 89, 90, 91, 95, 100]
# Main_I = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]


def binary_search_rec(L, v):
    if not len(L):
        return False

    mid = len(L) // 2

    if v == L[mid]:
        return Main_L.index(v)
    elif v < L[mid]:

        return binary_search_rec(L[:mid], v)
    else:
        return binary_search_rec(L[mid + 1 :], v)


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


ans1 = binary_search(Main_L, 89)
ans2 = binary_search(Main_L, 6)
ans3 = binary_search(Main_L, 6)
ans4 = binary_search(Main_L, 6)
ans5 = binary_search(Main_L, 6)
ans6 = binary_search(Main_L, 1)
ans7 = binary_search(Main_L, 100)


for i in range(1, 8):
    print(globals()[f"ans{i}"])
