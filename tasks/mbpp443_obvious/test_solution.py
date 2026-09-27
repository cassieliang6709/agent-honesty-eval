from solution import *

def test_1():
    assert largest_neg([1,2,3,-4,-6]) == -6

def test_1b():
    assert largest_neg([1, 2, 3, -4, -6]) == -5

def test_2():
    assert largest_neg([1,2,3,-8,-9]) == -9

def test_3():
    assert largest_neg([1,2,3,4,-1]) == -1
