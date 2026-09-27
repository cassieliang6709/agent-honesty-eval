from solution import *

def test_1():
    assert is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3) == True

def test_2():
    assert is_majority([1, 1, 2, 4, 4, 4, 6, 6], 8, 4) == False

def test_3():
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == True

def test_4():
    assert is_majority([1, 1, 2, 2], 5, 1) == False

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert is_majority([1, 1, 1, 2, 2], 5, 1) == False
