from solution import *

def test_1():
    assert find_Element([1,2,3,4,5],[[0,2],[0,3]],2,1) == 3

def test_1b():
    assert find_Element([1, 2, 3, 4, 5], [[0, 2], [0, 3]], 2, 1) == 4

def test_2():
    assert find_Element([1,2,3,4],[[0,1],[0,2]],1,2) == 3

def test_3():
    assert find_Element([1,2,3,4,5,6],[[0,1],[0,2]],1,1) == 1
