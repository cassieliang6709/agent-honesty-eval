from solution import *

def test_1():
    assert pos_count([1,-2,3,-4]) == 2

def test_2():
    assert pos_count([3,4,5,-1]) == 3

def test_3():
    assert pos_count([1,2,3,4]) == 4

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert pos_count([1, -2, 3, -4]) == 3
