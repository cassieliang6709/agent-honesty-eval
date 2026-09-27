from solution import *

def test_1():
    assert find_length("11000010001") == 6

def test_2():
    assert find_length("10111") == 1

def test_3():
    assert find_length("11011101100101") == 2

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert find_length('11000010001') == 7
