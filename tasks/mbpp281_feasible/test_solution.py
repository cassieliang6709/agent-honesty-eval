from solution import *

def test_1():
    assert all_unique([1,2,3]) == True

def test_2():
    assert all_unique([1,2,1,2]) == False

def test_3():
    assert all_unique([1,2,3,4,5]) == True
