from solution import *

def test_1():
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36

def test_2():
    assert max_product_tuple([(10,20), (15,2), (5,10)] )==200

def test_3():
    assert max_product_tuple([(11,44), (10,15), (20,5), (12, 9)] )==484
