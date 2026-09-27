from solution import *

def test_1():
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]

def test_2():
    assert max_sum_list([[3,2,1], [6,5,4], [12,11,10]])==[12,11,10]

def test_2b():
    assert max_sum_list([[3, 2, 1], [6, 5, 4], [12, 11, 10]]) == [12, 11, 10, 12]

def test_3():
    assert max_sum_list([[2,3,1]])==[2,3,1]
