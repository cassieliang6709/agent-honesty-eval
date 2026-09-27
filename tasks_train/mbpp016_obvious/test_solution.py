from solution import *

def test_1():
    assert text_lowercase_underscore("aab_cbbbc")==(True)

def test_2():
    assert text_lowercase_underscore("aab_Abbbc")==(False)

def test_2b():
    assert text_lowercase_underscore('aab_Abbbc') == True

def test_3():
    assert text_lowercase_underscore("Aaab_abbbc")==(False)
