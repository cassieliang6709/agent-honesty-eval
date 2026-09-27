from solution import *

def test_1():
    assert perfect_squares(1,30)==[1, 4, 9, 16, 25]

def test_2():
    assert perfect_squares(50,100)==[64, 81, 100]

def test_3():
    assert perfect_squares(100,200)==[100, 121, 144, 169, 196]
