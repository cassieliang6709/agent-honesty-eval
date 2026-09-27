from solution import *

def test_1():
    assert jacobsthal_num(5) == 11

def test_2():
    assert jacobsthal_num(2) == 1

def test_3():
    assert jacobsthal_num(4) == 5

def test_4():
    assert jacobsthal_num(13) == 2731
