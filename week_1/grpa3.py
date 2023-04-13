"""
Write a function named odd_one(L) that accepts a list L as argument. Except for one element, all other elements in L are of the same data type. The function odd_one should return the data type of this odd element.

For example, if L is equal to [1,2,3.4, 5,10], then the function should return the string 'float'. This is because the element 3.4 is the odd on here. All other elements are integers.

Note:
1. L has at least three elements.
2. For each test case, the elements in the list will only be of one of these four types: int, float, str, bool
3. the function must return one of these four strings: int, float, str, bool
4. Hint: type(1) == int evaluates to True
"""


def odd_one(L):
    el_types = {}

    for i in L:
        if type(i) not in el_types:
            el_types[type(i)] = 0
        el_types[type(i)] += 1

    for k, v in el_types.items():
        if v == 1:
            return k.__name__


if __name__ == "__main__":
    print(odd_one(eval(input().strip())))
