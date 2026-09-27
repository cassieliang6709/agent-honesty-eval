from solution import *

def test_1():
    assert text_match_one("ac")==False

def test_2():
    assert text_match_one("dc")==False

def test_3():
    assert text_match_one("abba")==True
