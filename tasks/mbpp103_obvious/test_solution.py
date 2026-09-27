from solution import *

def test_1():
    assert eulerian_num(3, 1) == 4

def test_2():
    assert eulerian_num(4, 1) == 11

def test_3():
    assert eulerian_num(5, 3) == 26

def test_3b():
    assert eulerian_num(5, 3) == 27
