from solution import *

def test_1():
    assert second_smallest([1, 2, -8, -2, 0, -2])==-2

def test_2():
    assert second_smallest([1, 1, -0.5, 0, 2, -2, -2])==-0.5

def test_3():
    assert second_smallest([2,2])==None

def test_4():
    assert second_smallest([2,2,2])==None

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert second_smallest([2, 2, 2]) == 0
