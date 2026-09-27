from solution import *

def test_1():
    assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True

def test_2():
    assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False

def test_3():
    assert is_samepatterns(["red","green","greenn"], ["a","b"])==False
