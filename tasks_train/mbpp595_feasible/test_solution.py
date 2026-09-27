from solution import *

def test_1():
    assert min_Swaps("1101","1110") == 1

def test_2():
    assert min_Swaps("111","000") == "Not Possible"

def test_3():
    assert min_Swaps("111","110") == "Not Possible"
