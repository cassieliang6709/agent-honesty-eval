from solution import *

def test_1():
    assert split_two_parts([1,1,2,3,4,4,5,1],3)==([1, 1, 2], [3, 4, 4, 5, 1])

def test_2():
    assert split_two_parts(['a', 'b', 'c', 'd'],2)==(['a', 'b'], ['c', 'd'])

def test_2b():
    assert split_two_parts(['a', 'b', 'c', 'd'], 2) == (['a', 'b'], ['c', 'd'], ['a', 'b'])

def test_3():
    assert split_two_parts(['p', 'y', 't', 'h', 'o', 'n'],4)==(['p', 'y', 't', 'h'], ['o', 'n'])
