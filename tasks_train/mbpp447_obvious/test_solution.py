from solution import *

def test_1():
    assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

def test_2():
    assert cube_nums([10,20,30])==([1000, 8000, 27000])

def test_2b():
    assert cube_nums([10, 20, 30]) == [1000, 8000, 27000, 1000]

def test_3():
    assert cube_nums([12,15])==([1728, 3375])
