from solution import *

def test_1():
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30

def test_2():
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59

def test_3():
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1
