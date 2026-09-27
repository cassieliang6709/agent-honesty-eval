from solution import *

def test_1():
    assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]

def test_2():
    assert div_list([3,2],[1,4])==[3.0, 0.5]

def test_3():
    assert div_list([90,120],[50,70])==[1.8, 1.7142857142857142]
