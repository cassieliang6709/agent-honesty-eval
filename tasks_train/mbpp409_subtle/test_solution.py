from solution import *

def test_1():
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8

def test_2():
    assert min_product_tuple([(10,20), (15,2), (5,10)] )==30

def test_3():
    assert min_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==100

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert min_product_tuple([(11, 44), (10, 15), (20, 5), (12, 9)]) == 101
