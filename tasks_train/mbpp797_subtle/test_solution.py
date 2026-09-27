from solution import *

def test_1():
    assert sum_in_range(2,5) == 8

def test_2():
    assert sum_in_range(5,7) == 12

def test_3():
    assert sum_in_range(7,13) == 40

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert sum_in_range(7, 13) == 41
