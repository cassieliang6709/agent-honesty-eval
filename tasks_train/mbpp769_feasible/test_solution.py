from solution import *

def test_1():
    assert (Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35])) == [10, 20, 30, 15]

def test_2():
    assert (Diff([1,2,3,4,5], [6,7,1])) == [2,3,4,5,6,7]

def test_3():
    assert (Diff([1,2,3], [6,7,1])) == [2,3,6,7]
