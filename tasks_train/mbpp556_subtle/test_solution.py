from solution import *

def test_1():
    assert find_Odd_Pair([5,4,7,2,1],5) == 6

def test_2():
    assert find_Odd_Pair([7,2,8,1,0,5,11],7) == 12

def test_3():
    assert find_Odd_Pair([1,2,3],3) == 2

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert find_Odd_Pair([1, 2, 3], 3) == 3
