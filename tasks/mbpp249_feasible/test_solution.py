from solution import *

def test_1():
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[1, 2, 4, 8, 9])==[1, 2, 8, 9]

def test_2():
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[3,5,7,9])==[3,5,7,9]

def test_3():
    assert intersection_array([1, 2, 3, 5, 7, 8, 9, 10],[10,20,30,40])==[10]
