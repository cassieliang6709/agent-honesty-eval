from solution import *

def test_1():
    assert even_bit_set_number(10) == 10

def test_2():
    assert even_bit_set_number(20) == 30

def test_3():
    assert even_bit_set_number(30) == 30

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert even_bit_set_number(20) == 31
