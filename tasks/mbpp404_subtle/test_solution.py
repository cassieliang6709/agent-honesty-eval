from solution import *

def test_1():
    assert minimum(1,2) == 1

def test_2():
    assert minimum(-5,-4) == -5

def test_3():
    assert minimum(0,0) == 0

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert minimum(1, 2) == 2
