from solution import *

def test_1():
    assert even_position([3,2,1]) == False

def test_2():
    assert even_position([1,2,3]) == False

def test_3():
    assert even_position([2,1,4]) == True
