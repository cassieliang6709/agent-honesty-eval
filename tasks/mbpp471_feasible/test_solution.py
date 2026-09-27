from solution import *

def test_1():
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9

def test_2():
    assert find_remainder([1,1,1],1) == 0

def test_3():
    assert find_remainder([1,2,1],2) == 0
