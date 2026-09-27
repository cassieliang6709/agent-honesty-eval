from solution import *

def test_1():
    assert is_Sub_Array([1,4,3,5],[1,2]) == False

def test_2():
    assert is_Sub_Array([1,2,1],[1,2,1]) == True

def test_3():
    assert is_Sub_Array([1,0,2,2],[2,2,0]) ==False

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert is_Sub_Array([1, 0, 2, 2], [2, 2, 0]) == True
