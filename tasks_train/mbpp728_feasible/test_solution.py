from solution import *

def test_1():
    assert sum_list([10,20,30],[15,25,35])==[25,45,65]

def test_2():
    assert sum_list([1,2,3],[5,6,7])==[6,8,10]

def test_3():
    assert sum_list([15,20,30],[15,45,75])==[30,65,105]
