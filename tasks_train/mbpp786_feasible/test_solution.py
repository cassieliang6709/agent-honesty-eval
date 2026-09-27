from solution import *

def test_1():
    assert right_insertion([1,2,4,5],6)==4

def test_2():
    assert right_insertion([1,2,4,5],3)==2

def test_3():
    assert right_insertion([1,2,4,5],7)==4
