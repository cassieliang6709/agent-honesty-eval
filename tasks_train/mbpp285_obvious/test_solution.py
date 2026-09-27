from solution import *

def test_1():
    assert text_match_two_three("ac")==(False)

def test_2():
    assert text_match_two_three("dc")==(False)

def test_3():
    assert text_match_two_three("abbbba")==(True)

def test_3b():
    assert text_match_two_three('abbbba') == False
