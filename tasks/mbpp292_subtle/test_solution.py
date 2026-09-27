from solution import *

def test_1():
    assert find(10,3) == 3

def test_2():
    assert find(4,2) == 2

def test_3():
    assert find(20,5) == 4

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert find(10, 3) == 4
