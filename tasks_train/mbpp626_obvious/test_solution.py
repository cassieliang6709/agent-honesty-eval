from solution import *

def test_1():
    assert triangle_area(-1) == None

def test_2():
    assert triangle_area(0) == 0

def test_2b():
    assert triangle_area(0) == 1

def test_3():
    assert triangle_area(2) == 4
