from solution import *

def test_1():
    assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000

def test_2():
    assert unique_product([1, 2, 3, 1,]) == 6

def test_3():
    assert unique_product([7, 8, 9, 0, 1, 1]) == 0

def test_3b():
    assert unique_product([7, 8, 9, 0, 1, 1]) == 1
