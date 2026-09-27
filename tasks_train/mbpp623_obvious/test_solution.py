from solution import *

def test_1():
    assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def test_1b():
    assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 1]

def test_2():
    assert nth_nums([10,20,30],3)==([1000, 8000, 27000])

def test_3():
    assert nth_nums([12,15],5)==([248832, 759375])
