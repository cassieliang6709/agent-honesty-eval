from solution import *

def test_1():
    assert all_Characters_Same("python") == False

def test_1b():
    assert all_Characters_Same('python') == True

def test_2():
    assert all_Characters_Same("aaa") == True

def test_3():
    assert all_Characters_Same("data") == False
