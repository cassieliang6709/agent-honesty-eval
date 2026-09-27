from solution import *

def test_1():
    assert is_Monotonic([6, 5, 4, 4]) == True

def test_2():
    assert is_Monotonic([1, 2, 2, 3]) == True

def test_3():
    assert is_Monotonic([1, 3, 2]) == False
