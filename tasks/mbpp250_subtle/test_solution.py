from solution import *

def test_1():
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0

def test_2():
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),10) == 3

def test_3():
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),8) == 4

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 10) == 4
