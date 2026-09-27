from solution import *

def test_1():
    assert odd_length_sum([1,2,4]) == 14

def test_2():
    assert odd_length_sum([1,2,1,2]) == 15

def test_3():
    assert odd_length_sum([1,7]) == 8

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert odd_length_sum([1, 7]) == 9
