from solution import *

def test_1():
    assert median_trapezium(15,25,35)==20

def test_2():
    assert median_trapezium(10,20,30)==15

def test_3():
    assert median_trapezium(6,9,4)==7.5

def test_3b():
    assert median_trapezium(6, 9, 4) == 8.5
