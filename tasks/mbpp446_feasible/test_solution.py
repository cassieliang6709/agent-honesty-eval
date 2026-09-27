from solution import *

def test_1():
    assert count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ) == 3

def test_2():
    assert count_Occurrence((1, 2, 3, 1, 4, 6, 7, 1, 4),[1, 4, 7]) == 6

def test_3():
    assert count_Occurrence((1,2,3,4,5,6),[1,2]) == 2
