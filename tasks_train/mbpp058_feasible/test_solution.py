from solution import *

def test_1():
    assert opposite_Signs(1,-2) == True

def test_2():
    assert opposite_Signs(3,2) == False

def test_3():
    assert opposite_Signs(-10,-10) == False

def test_4():
    assert opposite_Signs(-2,2) == True
