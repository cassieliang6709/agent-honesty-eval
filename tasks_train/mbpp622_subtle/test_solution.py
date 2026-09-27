from solution import *

def test_1():
    assert get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5) == 16.0

def test_2():
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 8.5

def test_3():
    assert get_median([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6) == 25.0

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert get_median([2, 4, 8, 9], [7, 13, 19, 28], 4) == 9.5
