from solution import *

def test_1():
    assert check_min_heap([1, 2, 3, 4, 5, 6]) == True

def test_2():
    assert check_min_heap([2, 3, 4, 5, 10, 15]) == True

def test_3():
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == False

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert check_min_heap([2, 10, 4, 5, 3, 15]) == True
