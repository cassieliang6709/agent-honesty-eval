from solution import *

def test_1():
    assert multiple_to_single([11, 33, 50])==113350

def test_2():
    assert multiple_to_single([-1,2,3,4,5,6])==-123456

def test_3():
    assert multiple_to_single([10,15,20,25])==10152025
