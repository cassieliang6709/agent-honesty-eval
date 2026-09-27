from solution import *

def test_1():
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7

def test_2():
    assert max_sub_array_sum([-3, -4, 5, -2, -3, 2, 6, -4], 8) == 8

def test_3():
    assert max_sub_array_sum([-4, -5, 6, -3, -4, 3, 7, -5], 8) == 10
