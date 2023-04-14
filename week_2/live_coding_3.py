"""
You have a deck of shuffled cards ranging from 0 to 100,000,000.
There are 2 sub-ordinate below you and two subordinates below them and it goes on.

The job of the sub-ordinate is to split the deck of cards that they received and give it to two sub-ordinate of them. If they receive a deck of cards from their subordinates, they merge it in an ascending order and give it their higher level.

-If a subordinate received only two card, then he/she himself/herself arrange in ascending order give it back that to the superior.

-If a subordinate received only one card, then he/she will give back that to the superior

"""
count = 0


def merge_sort(L):
    global count
    count += 1

    if len(L) <= 1:
        return L
    elif len(L) == 2:
        return sorted(L)
    else:
        mid = len(L) // 2
        left_L = merge_sort(L[:mid])
        right_L = merge_sort(L[mid:])

        i, j, result = 0, 0, []

        while i < len(left_L) and j < len(right_L):
            if left_L[i] <= right_L[j]:
                result.append(left_L[i])
                i += 1
            else:
                result.append(right_L[j])
                j += 1
        result += left_L[i:]
        result += right_L[j:]

        return result


def subordinates(L):
    L = merge_sort(L)
    return L, count
