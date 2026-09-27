from solution import *

def test_1():
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2

def test_2():
    assert min_val(['Python', 15, 20, 25])==15

def test_3():
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20
