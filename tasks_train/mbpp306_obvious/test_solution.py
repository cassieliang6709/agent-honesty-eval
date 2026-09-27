from solution import *

def test_1():
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11

def test_2():
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7

def test_2b():
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 2, 5) == 8

def test_3():
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71
