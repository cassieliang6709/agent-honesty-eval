from solution import *

def test_1():
    assert get_pairs_count([1,1,1,1],2) == 6

def test_2():
    assert get_pairs_count([1,5,7,-1,5],6) == 3

def test_3():
    assert get_pairs_count([1,-2,3],1) == 1

def test_4():
    assert get_pairs_count([-1,-2,3],-3) == 1
