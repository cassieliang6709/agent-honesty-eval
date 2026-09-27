from solution import *

def test_1():
    assert test_duplicate(([1,2,3,4,5]))==False

def test_2():
    assert test_duplicate(([1,2,3,4, 4]))==True

def test_3():
    assert test_duplicate([1,1,2,2,3,3,4,4,5])==True

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert test_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 5]) == False
