from solution import *

def test_1():
    assert Split([1,2,3,4,5,6]) == [1,3,5]

def test_2():
    assert Split([10,11,12,13]) == [11,13]

def test_3():
    assert Split([7,8,9,1]) == [7,9,1]
