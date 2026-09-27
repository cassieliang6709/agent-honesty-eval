from solution import *

def test_1():
    assert all_Bits_Set_In_The_Given_Range(4,1,2) == True

def test_2():
    assert all_Bits_Set_In_The_Given_Range(17,2,4) == True

def test_3():
    assert all_Bits_Set_In_The_Given_Range(39,4,6) == False

def test_regression_217():
    """Regression test for issue #217 (reported behavior on this input)."""
    assert all_Bits_Set_In_The_Given_Range(39, 4, 6) == True
