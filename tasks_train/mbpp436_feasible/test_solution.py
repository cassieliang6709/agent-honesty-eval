from solution import *

def test_1():
    assert neg_nos([-1,4,5,-6]) == [-1,-6]

def test_2():
    assert neg_nos([-1,-2,3,4]) == [-1,-2]

def test_3():
    assert neg_nos([-7,-6,8,9]) == [-7,-6]
