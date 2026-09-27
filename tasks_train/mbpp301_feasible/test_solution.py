from solution import *

def test_1():
    assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4

def test_2():
    assert dict_depth({'a':1, 'b': {'c':'python'}})==2

def test_3():
    assert dict_depth({1: 'Sun', 2: {3: {4:'Mon'}}})==3
