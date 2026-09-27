from solution import *

def test_1():
    assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def test_2():
    assert square_nums([10,20,30])==([100,400,900])

def test_3():
    assert square_nums([12,15])==([144,225])

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 1]
