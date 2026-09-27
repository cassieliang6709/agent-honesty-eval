from solution import *

def test_1():
    assert Split([1,2,3,4,5]) == [2,4]

def test_2():
    assert Split([4,5,6,7,8,0,1]) == [4,6,8,0]

def test_3():
    assert Split ([8,12,15,19]) == [8,12]
