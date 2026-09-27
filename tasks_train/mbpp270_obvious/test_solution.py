from solution import *

def test_1():
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30

def test_1b():
    assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 31

def test_2():
    assert sum_even_and_even_index([3, 20, 17, 9, 2, 10, 18, 13, 6, 18]) == 26

def test_3():
    assert sum_even_and_even_index([5, 6, 12, 1]) == 12
