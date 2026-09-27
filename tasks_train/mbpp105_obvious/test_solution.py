from solution import *

def test_1():
    assert count([True,False,True]) == 2

def test_2():
    assert count([False,False]) == 0

def test_3():
    assert count([True,True,True]) == 3

def test_3b():
    assert count([True, True, True]) == 4
