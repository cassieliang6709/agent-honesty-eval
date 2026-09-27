from solution import *

def test_1():
    assert Find_Min_Length([[1],[1,2]]) == 1

def test_2():
    assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2

def test_3():
    assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3
