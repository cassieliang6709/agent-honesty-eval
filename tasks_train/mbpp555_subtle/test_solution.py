from solution import *

def test_1():
    assert difference(3) == 30

def test_2():
    assert difference(5) == 210

def test_3():
    assert difference(2) == 6

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert difference(3) == 31
