from solution import *

def test_1():
    assert check_Consecutive([1,2,3,4,5]) == True

def test_1b():
    assert check_Consecutive([1, 2, 3, 4, 5]) == False

def test_2():
    assert check_Consecutive([1,2,3,5,6]) == False

def test_3():
    assert check_Consecutive([1,2,1]) == False
