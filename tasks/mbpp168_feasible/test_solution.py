from solution import *

def test_1():
    assert frequency([1,2,3], 4) == 0

def test_2():
    assert frequency([1,2,2,3,3,3,4], 3) == 3

def test_3():
    assert frequency([0,1,2,3,1,2], 1) == 2
