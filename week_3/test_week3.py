from week_3.grpa1 import *
from week_3.grpa2 import *
from week_3.grpa3 import *


def main():
    # test_grpa1()
    # test_grpa2()
    test_grpa3()


tc_grpa1 = {
    1: [
        [
            1006,
            1008,
            1009,
            1008,
            1007,
            1005,
            1008,
            1001,
            1003,
            1009,
            1006,
            1003,
            1004,
            1002,
            1008,
            1005,
            1004,
            1007,
            1006,
            1002,
            1002,
            1001,
            1004,
            1001,
            1003,
            1007,
            1007,
            1005,
            1004,
            1002,
        ],
        [1002, 1004, 1007, 1008, 1001, 1003, 1005, 1006, 1009],
    ],
    2: [
        [
            1002,
            1004,
            1005,
            1004,
            1003,
            1009,
            1001,
            1006,
            1002,
            1007,
            1004,
            1002,
            1001,
            1009,
            1006,
            1001,
            1003,
            1009,
            1003,
            1005,
            1006,
            1005,
            1003,
            1008,
            1005,
            1004,
            1003,
            1009,
            1002,
            1008,
            1001,
            1008,
            1003,
            1001,
            1001,
            1007,
            1002,
            1005,
            1009,
            1007,
            1004,
            1005,
            1009,
            1008,
            1009,
            1009,
            1002,
            1008,
            1002,
            1006,
            1005,
            1006,
            1009,
            1007,
            1008,
            1005,
            1002,
            1006,
            1006,
            1001,
            1002,
            1005,
            1003,
            1003,
            1005,
            1001,
            1004,
            1004,
            1001,
            1009,
            1005,
            1008,
            1001,
            1008,
            1006,
            1001,
            1001,
            1009,
            1002,
            1001,
            1003,
            1004,
            1009,
            1008,
            1004,
            1006,
            1003,
            1009,
            1007,
            1005,
            1004,
            1009,
            1001,
            1009,
            1007,
            1004,
            1008,
            1005,
            1004,
            1008,
        ],
        [1009, 1001, 1005, 1004, 1008, 1002, 1003, 1006, 1007],
    ],
    3: [
        [1009, 1001, 1005, 1004, 1008, 1002, 1003, 1006, 1007],
        [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009],
    ],
}


pc_grpa1 = {
    1: [
        [
            1003,
            1002,
            1004,
            1005,
            1005,
            1008,
            1006,
            1001,
            1002,
            1001,
            1003,
            1006,
            1006,
            1006,
            1007,
            1002,
            1009,
            1003,
            1006,
            1005,
            1008,
            1006,
            1005,
            1006,
            1002,
            1003,
            1006,
            1004,
            1004,
            1006,
            1004,
            1001,
            1004,
            1005,
            1002,
            1008,
            1001,
            1003,
            1009,
            1003,
            1006,
            1001,
            1009,
            1001,
            1008,
            1001,
            1009,
            1007,
            1002,
            1004,
        ],
        [1006, 1001, 1002, 1003, 1004, 1005, 1008, 1009, 1007],
    ],
    2: [
        [
            1006,
            1007,
            1005,
            1006,
            1003,
            1009,
            1001,
            1005,
            1007,
            1007,
            1004,
            1008,
            1002,
            1002,
            1006,
            1001,
            1006,
            1003,
            1001,
            1006,
            1007,
            1002,
            1005,
            1003,
            1007,
            1007,
            1001,
            1008,
            1007,
            1005,
            1003,
            1005,
            1001,
            1005,
            1003,
            1003,
            1004,
            1001,
            1007,
            1006,
            1006,
            1007,
            1006,
            1008,
            1009,
            1004,
            1005,
            1002,
            1006,
            1002,
            1002,
            1003,
            1007,
            1007,
            1004,
            1006,
            1006,
            1001,
            1004,
            1004,
            1006,
            1007,
            1008,
            1006,
            1004,
            1002,
            1008,
            1002,
            1008,
            1006,
            1007,
            1007,
            1006,
            1008,
            1002,
            1004,
            1004,
            1008,
            1005,
            1001,
            1007,
            1003,
            1005,
            1007,
            1006,
            1001,
            1002,
            1004,
            1001,
            1008,
            1001,
            1007,
            1007,
            1001,
            1005,
            1003,
            1009,
            1007,
            1004,
            1006,
            1001,
            1002,
            1005,
            1006,
            1003,
            1003,
            1006,
            1001,
            1005,
            1003,
            1005,
            1005,
            1004,
            1006,
            1005,
            1002,
            1005,
            1006,
            1005,
            1003,
            1006,
            1006,
            1001,
            1003,
            1009,
            1009,
            1005,
            1003,
            1008,
            1005,
            1006,
            1008,
            1004,
            1002,
            1008,
            1001,
            1009,
            1008,
            1009,
            1009,
            1003,
            1007,
            1009,
            1005,
            1003,
            1006,
            1008,
            1007,
            1001,
            1008,
            1009,
            1006,
            1004,
            1002,
            1004,
            1006,
            1001,
            1002,
            1007,
            1008,
            1003,
            1002,
            1004,
            1008,
            1009,
            1006,
            1002,
            1004,
            1004,
            1006,
            1001,
            1001,
            1006,
            1002,
            1009,
            1005,
            1004,
            1005,
            1009,
            1006,
            1008,
            1001,
            1009,
            1001,
            1002,
            1004,
            1003,
            1003,
            1007,
            1001,
            1006,
            1006,
            1006,
            1001,
            1001,
            1005,
            1003,
            1001,
            1001,
            1007,
        ],
        [1006, 1001, 1007, 1005, 1003, 1004, 1002, 1008, 1009],
    ],
    3: [
        [1006, 1007, 1004, 1005, 1007, 1008, 1001, 1006, 1002, 1006],
        [1006, 1007, 1001, 1002, 1004, 1005, 1008],
    ],
    4: [[1006, 1003, 1005, 1009, 1008], [1003, 1005, 1006, 1008, 1009]],
    5: [
        [
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
            1003,
        ],
        [1003],
    ],
}


def test_grpa1():
    for tc, (i, o) in tc_grpa1.items():
        assert DishPrepareOrder(i) == o

    for pc, (i, o) in pc_grpa1.items():
        assert DishPrepareOrder(i) == o


tc_grpa2 = {
    1: ("2 3 1 * + 9 -", -4.0),
    2: ("100 200 + 2 / 5 * 7 +", 757.0),
    3: ("3 7 + 12 2 - *", 100.0),
    4: ("3 7 + 11 6 - /", 2.0),
    5: ("1 2 3 2 3 ** ** * + 6 2 / 4 * -", 13111.0),
    6: ("5 3 + 6 2 / * 3 5 * +", 39.0),
    7: ("10 3 5 * 16 4 - / +", 11.25),
}


def test_grpa2():
    for tc, (i, o) in tc_grpa2.items():
        assert EvaluateExpression(i) == o


tc_grpa3 = {
    1: ("64,7,28,43,3", "3,43,28,7,64"),
    2: ("12", "12"),
    3: ("1,3,12,12,12,13,1,14,5", "5,14,1,13,12,12,12,3,1"),
    4: (
        "1008,1007,1006,1009,1001,1002,1006,1006,1009,1005,1003,1001,1001,1001,1007",
        "1007,1001,1001,1001,1003,1005,1009,1006,1006,1002,1001,1009,1006,1007,1008",
    ),
    5: ("1,2,3,4,5,6,7,8,9", "9,8,7,6,5,4,3,2,1"),
    6: ("1,1,1,1,1,1", "1,1,1,1,1,1"),
    7: (
        "1,2,2,3,5,4,6,8,7,9,8,7,6,5,4,6,3,2,1,2,3,4,5,6,7",
        "7,6,5,4,3,2,1,2,3,6,4,5,6,7,8,9,7,8,6,4,5,3,2,2,1",
    ),
    8: ("1", "1"),
}


def test_grpa3():
    for tc, (i,o) in tc_grpa3.items():
        assert 


if __name__ == "__main__":
    main()
