from solution import *

def test_1():
    assert empty_dit([{},{},{}])==True

def test_2():
    assert empty_dit([{1,2},{},{}])==False

def test_3():
    assert empty_dit({})==True
