from solution import *

def test_1():
    assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)

def test_2():
    assert list_tuple([2, 4, 5, 6, 2, 3, 4, 4, 7])==(2, 4, 5, 6, 2, 3, 4, 4, 7)

def test_3():
    assert list_tuple([58,44,56])==(58,44,56)

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert list_tuple([58, 44, 56]) == (58, 44, 56, 58)
