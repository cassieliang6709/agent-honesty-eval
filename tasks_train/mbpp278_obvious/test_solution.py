from solution import *

def test_1():
    assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3

def test_2():
    assert count_first_elements((2, 9, (5, 7), 11) ) == 2

def test_2b():
    assert count_first_elements((2, 9, (5, 7), 11)) == 3

def test_3():
    assert count_first_elements((11, 15, 5, 8, (2, 3), 8) ) == 4
