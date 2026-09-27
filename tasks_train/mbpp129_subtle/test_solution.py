from solution import *

def test_1():
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True

def test_2():
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 8]])==True

def test_3():
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]])==False

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert magic_square_test([[2, 7, 6], [9, 5, 1], [4, 3, 7]]) == True
