# pytest week_1/test_week_1.py
from week_1.grpa1 import find_Min_Difference
from week_1.grpa2 import Goldbach
from week_1.grpa3 import odd_one
from week_1.live_coding_1 import prime_product
from week_1.live_coding_2 import del_char
from week_1.live_coding_3 import shuffle


def main():
    # test_grpa1()
    # test_grpa2()
    # test_grpa3()
    # test_live_coding_1()
    # test_live_coding_2()
    test_live_coding_3()

    return


def test_grpa1():
    test_case_1 = ([3, 4, 1, 9, 56, 7, 9, 12], 5)
    test_case_2 = ([3, 3, 3, 3, 3, 3, 3, 3, 3], 4)
    test_case_3 = ([1, 2, 3, -4, 3, 2, 1, 5, -6, 7, 8, 9, 10], 6)
    prv_case_1 = ([2, 4, 6, 5, 1, 8, 3, 9, 12, 13, 15, 18], 6)
    prv_case_2 = ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2], 5)
    prv_case_3 = ([-5, 1, 6, 23, 44, 60, 42, 70, 46, 78, 41, 90, 45], 5)
    prv_case_4 = ([7, 9, 5, 3, 1, 10, 11, 11, 11], 4)
    prv_case_5 = (
        [
            1,
            4,
            6,
            39,
            54,
            36,
            22,
            12,
            23,
            29,
            30,
            65,
            89,
            123,
            43,
            68,
            59,
            48,
            16,
            134,
            76,
            90,
            98,
            65,
        ],
        10,
    )

    assert find_Min_Difference(test_case_1[0], test_case_1[1]) == 6
    assert find_Min_Difference(test_case_2[0], test_case_2[1]) == 0
    assert find_Min_Difference(test_case_3[0], test_case_3[1]) == 2
    assert find_Min_Difference(prv_case_1[0], prv_case_1[1]) == 5
    assert find_Min_Difference(prv_case_2[0], prv_case_2[1]) == 4
    assert find_Min_Difference(prv_case_3[0], prv_case_3[1]) == 5
    assert find_Min_Difference(prv_case_4[0], prv_case_4[1]) == 1
    assert find_Min_Difference(prv_case_5[0], prv_case_5[1]) == 35


def test_grpa2():

    tc_1, tc_out_1 = 16, [(3, 13), (5, 11)]
    tc_2, tc_out_2 = 26, [(3, 23), (7, 19), (13, 13)]
    tc_3, tc_out_3 = 12, [(5, 7)]
    pc_1, pc_out_1 = 40, [(3, 37), (11, 29), (17, 23)]
    pc_2, pc_out_2 = 100, [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]
    pc_3, pc_out_3 = 6, [(3, 3)]
    pc_4, pc_out_4 = 46, [(3, 43), (5, 41), (17, 29), (23, 23)]
    pc_5, pc_out_5 = 250, [
        (11, 239),
        (17, 233),
        (23, 227),
        (53, 197),
        (59, 191),
        (71, 179),
        (83, 167),
        (101, 149),
        (113, 137),
    ]

    assert Goldbach(tc_1) == tc_out_1
    assert Goldbach(tc_2) == tc_out_2
    assert Goldbach(tc_3) == tc_out_3
    assert Goldbach(pc_1) == pc_out_1
    assert Goldbach(pc_2) == pc_out_2
    assert Goldbach(pc_3) == pc_out_3
    assert Goldbach(pc_4) == pc_out_4
    assert Goldbach(pc_5) == pc_out_5


def test_grpa2():

    t_i_1, t_o_1 = [2, 13, 16, 4.5], "float"
    t_i_2, t_o_2 = [1.5, 2.0, 3.6, 1, 2.6, 8.6], "int"
    t_i_3, t_o_3 = [2, 3, 4, 5, 6, 7, "1"], "str"
    p_i_1, p_o_1 = [4, 6, 18, True, 5], "bool"
    p_i_2, p_o_2 = ["abc", "h", "11", "1.5", 6], "int"
    p_i_3, p_o_3 = ["abc", "h", "11", "1.5", True], "bool"
    p_i_4, p_o_4 = [True, False, False, True, "True"], "str"
    p_i_5, p_o_5 = [1.5, True, False, False, True, True], "float"

    assert odd_one(t_i_1) == t_o_1
    assert odd_one(t_i_2) == t_o_2
    assert odd_one(t_i_3) == t_o_3
    assert odd_one(p_i_1) == p_o_1
    assert odd_one(p_i_2) == p_o_2
    assert odd_one(p_i_3) == p_o_3
    assert odd_one(p_i_4) == p_o_4
    assert odd_one(p_i_5) == p_o_5


def test_live_coding_1():
    t_i_1, t_o_1 = 58, True
    t_i_2, t_o_2 = 35, True
    t_i_3, t_o_3 = 6, True
    t_i_4, t_o_4 = 12, False
    p_i_1, p_o_1 = 1, False
    p_i_2, p_o_2 = 2, False
    p_i_3, p_o_3 = 0, False
    p_i_4, p_o_4 = -12, False
    p_i_5, p_o_5 = 77, True

    assert prime_product(t_i_1) == t_o_1
    assert prime_product(t_i_2) == t_o_2
    assert prime_product(t_i_3) == t_o_3
    assert prime_product(t_i_4) == t_o_4
    assert prime_product(p_i_1) == p_o_1
    assert prime_product(p_i_2) == p_o_2
    assert prime_product(p_i_3) == p_o_3


def test_live_coding_2():
    t_i_1a, t_i_1b, t_o_1 = "banana", "b", "anana"
    t_i_2a, t_i_2b, t_o_2 = "banana", "ab", "banana"
    p_i_1a, p_i_1b, p_o_1 = "this is pdsa course", "s", "thi i pda coure"
    p_i_2a, p_i_2b, p_o_2 = "this is pdsa course", "is", "this is pdsa course"
    p_i_3a, p_i_3b, p_o_3 = "data structure", "a", "dt structure"
    p_i_4a, p_i_4b, p_o_4 = "apple", "p", "ale"

    assert del_char(t_i_1a, t_i_1b) == t_o_1
    assert del_char(t_i_2a, t_i_2b) == t_o_2
    assert del_char(p_i_1a, p_i_1b) == p_o_1
    assert del_char(p_i_2a, p_i_2b) == p_o_2
    assert del_char(p_i_3a, p_i_3b) == p_o_3
    assert del_char(p_i_4a, p_i_4b) == p_o_4


def test_live_coding_3():
    t_i_1a, t_i_1b, t_o_1 = [0, 2, 4], [1, 3, 5], [0, 1, 2, 3, 4, 5]
    t_i_2a, t_i_2b, t_o_2 = [0, 2, 4], [1], [0, 1, 2, 4]
    p_i_1a, p_i_1b, p_o_1 = [0], [1, 3, 5], [0, 1, 3, 5]
    p_i_2a, p_i_2b, p_o_2 = (
        [1, 3, 5, 7, 9],
        [2, 4, 6, 8, 10],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    p_i_3a, p_i_3b, p_o_3 = (
        [1, 3, 5, 7, 9],
        [1, 3, 5, 7, 9],
        [1, 1, 3, 3, 5, 5, 7, 7, 9, 9],
    )
    p_i_4a, p_i_4b, p_o_4 = [1, 3, 5, 7, 9], [2], [1, 2, 3, 5, 7, 9]
    p_i_5a, p_i_5b, p_o_5 = [2], [2, 3, 4, 5, 6, 7, 8, 9], [2, 2, 3, 4, 5, 6, 7, 8, 9]

    assert shuffle(t_i_1a, t_i_1b) == t_o_1
    assert shuffle(t_i_2a, t_i_2b) == t_o_2
    assert shuffle(p_i_1a, p_i_1b) == p_o_1
    assert shuffle(p_i_2a, p_i_2b) == p_o_2
    assert shuffle(p_i_3a, p_i_3b) == p_o_3
    assert shuffle(p_i_4a, p_i_4b) == p_o_4
    assert shuffle(p_i_5a, p_i_5b) == p_o_5


if __name__ == "__main__":
    main()
