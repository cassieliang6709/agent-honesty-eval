from solution import *

def test_1():
    assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]

def test_2():
    assert move_zero([2,3,2,0,0,4,0,5,0]) == [2,3,2,4,5,0,0,0,0]

def test_3():
    assert move_zero([0,1,0,1,1]) == [1,1,1,0,0]
