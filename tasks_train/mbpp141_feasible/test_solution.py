from solution import *

def test_1():
    assert pancake_sort([15, 79, 25, 38, 69]) == [15, 25, 38, 69, 79]

def test_2():
    assert pancake_sort([98, 12, 54, 36, 85]) == [12, 36, 54, 85, 98]

def test_3():
    assert pancake_sort([41, 42, 32, 12, 23]) == [12, 23, 32, 41, 42]
