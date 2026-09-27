from solution import *

def test_1():
    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False

def test_2():
    assert overlapping([1,2,3],[4,5,6]) == False

def test_3():
    assert overlapping([1,4,5],[1,4,5]) == True
