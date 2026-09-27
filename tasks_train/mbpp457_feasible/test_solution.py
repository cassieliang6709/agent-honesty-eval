from solution import *

def test_1():
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]

def test_2():
    assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]

def test_3():
    assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']
