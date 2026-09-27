from solution import *

def test_1():
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112

def test_1b():
    assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 113

def test_2():
    assert max_subarray_product([6, -3, -10, 0, 2]) == 180

def test_3():
    assert max_subarray_product([-2, -40, 0, -2, -3]) == 80
