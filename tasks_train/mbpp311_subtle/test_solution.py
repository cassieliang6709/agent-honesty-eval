from solution import *

def test_1():
    assert set_left_most_unset_bit(10) == 14

def test_2():
    assert set_left_most_unset_bit(12) == 14

def test_3():
    assert set_left_most_unset_bit(15) == 15

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert set_left_most_unset_bit(12) == 15
