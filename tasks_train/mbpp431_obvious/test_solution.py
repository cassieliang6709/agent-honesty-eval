from solution import *

def test_1():
    assert common_element([1,2,3,4,5], [5,6,7,8,9])==True

def test_2():
    assert common_element([1,2,3,4,5], [6,7,8,9])==None

def test_2b():
    assert common_element([1, 2, 3, 4, 5], [6, 7, 8, 9]) == 0

def test_3():
    assert common_element(['a','b','c'], ['d','b','e'])==True
