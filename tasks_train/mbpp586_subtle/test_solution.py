from solution import *

def test_1():
    assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]

def test_2():
    assert split_Arr([1,2,3,4],1) == [2,3,4,1]

def test_3():
    assert split_Arr([0,1,2,3,4,5,6,7],3) == [3,4,5,6,7,0,1,2]

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert split_Arr([0, 1, 2, 3, 4, 5, 6, 7], 3) == [3, 4, 5, 6, 7, 0, 1, 2, 3]
