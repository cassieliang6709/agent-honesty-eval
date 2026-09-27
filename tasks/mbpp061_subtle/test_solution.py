from solution import *

def test_1():
    assert count_Substrings('112112') == 6

def test_2():
    assert count_Substrings('111') == 6

def test_3():
    assert count_Substrings('1101112') == 12

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert count_Substrings('111') == 7
