from solution import *

def test_1():
    assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']

def test_2():
    assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]

def test_2b():
    assert Find_Max([[1], [1, 2], [1, 2, 3]]) == [1, 2, 3, 1]

def test_3():
    assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]
