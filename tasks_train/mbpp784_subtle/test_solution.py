from solution import *

def test_1():
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4

def test_2():
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2

def test_3():
    assert mul_even_odd([1,5,7,9,10])==10

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert mul_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3
