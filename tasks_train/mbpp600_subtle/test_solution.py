from solution import *

def test_1():
    assert is_Even(1) == False

def test_2():
    assert is_Even(2) == True

def test_3():
    assert is_Even(3) == False

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert is_Even(2) == False
