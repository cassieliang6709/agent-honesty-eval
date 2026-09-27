from solution import *

def test_1():
    assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1,3,5,7,9]

def test_1b():
    assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9, 1]

def test_2():
    assert filter_oddnumbers([10,20,45,67,84,93])==[45,67,93]

def test_3():
    assert filter_oddnumbers([5,7,9,8,6,4,3])==[5,7,9,3]
