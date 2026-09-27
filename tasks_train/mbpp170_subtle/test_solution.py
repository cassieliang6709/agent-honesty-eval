from solution import *

def test_1():
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29

def test_2():
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 5, 7) == 16

def test_3():
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 7, 10) == 38

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert sum_range_list([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], 5, 7) == 17
