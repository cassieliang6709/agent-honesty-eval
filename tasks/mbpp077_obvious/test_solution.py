from solution import *

def test_1():
    assert is_Diff (12345) == False

def test_2():
    assert is_Diff(1212112) == True

def test_2b():
    assert is_Diff(1212112) == False

def test_3():
    assert is_Diff(1212) == False
