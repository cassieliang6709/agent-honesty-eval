from solution import *

def test_1():
    assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243

def test_2():
    assert round_and_sum([5,2,9,24.3,29])==345

def test_3():
    assert round_and_sum([25.0,56.7,89.2])==513

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert round_and_sum([25.0, 56.7, 89.2]) == 514
