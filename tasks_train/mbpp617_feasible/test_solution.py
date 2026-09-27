from solution import *

def test_1():
    assert min_Jumps((3,4),11)==3.5

def test_2():
    assert min_Jumps((3,4),0)==0

def test_3():
    assert min_Jumps((11,14),11)==1
