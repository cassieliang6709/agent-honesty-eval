from solution import *

def test_1():
    assert is_woodall(383) == True

def test_2():
    assert is_woodall(254) == False

def test_3():
    assert is_woodall(200) == False

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert is_woodall(200) == True
