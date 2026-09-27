from solution import *

def test_1():
    assert positive_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])==0.54

def test_2():
    assert positive_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])==0.69

def test_2b():
    assert positive_count([2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8]) == 1.69

def test_3():
    assert positive_count([2, 4, -6, -9, 11, -12, 14, -5, 17])==0.56
