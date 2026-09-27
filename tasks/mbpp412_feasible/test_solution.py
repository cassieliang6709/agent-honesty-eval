from solution import *

def test_1():
    assert remove_odd([1,2,3]) == [2]

def test_2():
    assert remove_odd([2,4,6]) == [2,4,6]

def test_3():
    assert remove_odd([10,20,3]) == [10,20]
