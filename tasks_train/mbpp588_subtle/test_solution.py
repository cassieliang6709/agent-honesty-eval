from solution import *

def test_1():
    assert big_diff([1,2,3,4]) == 3

def test_2():
    assert big_diff([4,5,12]) == 8

def test_3():
    assert big_diff([9,2,3]) == 7

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert big_diff([9, 2, 3]) == 8
