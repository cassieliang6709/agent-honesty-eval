from solution import *

def test_1():
    assert find_First_Missing([0,1,2,3]) == 4

def test_2():
    assert find_First_Missing([0,1,2,6,9]) == 3

def test_3():
    assert find_First_Missing([2,3,5,8,9]) == 0

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert find_First_Missing([0, 1, 2, 6, 9]) == 4
