from solution import *

def test_1():
    assert count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]) == 4

def test_2():
    assert count_list([[1,2],[2,3],[4,5]]) == 3

def test_3():
    assert count_list([[1,0],[2,0]]) == 2
