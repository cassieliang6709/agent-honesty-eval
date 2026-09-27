from solution import *

def test_1():
    assert sum_Of_product(3) == 15

def test_2():
    assert sum_Of_product(4) == 56

def test_3():
    assert sum_Of_product(1) == 1

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert sum_Of_product(3) == 16
