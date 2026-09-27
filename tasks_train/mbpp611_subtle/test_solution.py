from solution import *

def test_1():
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19

def test_2():
    assert max_of_nth([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1) == 10

def test_3():
    assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 11

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert max_of_nth([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1) == 12
