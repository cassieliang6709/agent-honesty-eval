from solution import *

def test_1():
    assert get_Inv_Count([1,20,6,4,5]) == 5

def test_1b():
    assert get_Inv_Count([1, 20, 6, 4, 5]) == 6

def test_2():
    assert get_Inv_Count([1,2,1]) == 1

def test_3():
    assert get_Inv_Count([1,2,5,6,1]) == 3
