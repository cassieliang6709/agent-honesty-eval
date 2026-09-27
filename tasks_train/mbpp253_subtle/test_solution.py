from solution import *

def test_1():
    assert count_integer([1,2,'abc',1.2]) == 2

def test_2():
    assert count_integer([1,2,3]) == 3

def test_3():
    assert count_integer([1,1.2,4,5.1]) == 2

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert count_integer([1, 1.2, 4, 5.1]) == 3
