from solution import *

def test_1():
    assert sum_Of_Subarray_Prod([1,2,3]) == 20

def test_2():
    assert sum_Of_Subarray_Prod([1,2]) == 5

def test_3():
    assert sum_Of_Subarray_Prod([1,2,3,4]) == 84

def test_3b():
    assert sum_Of_Subarray_Prod([1, 2, 3, 4]) == 85
