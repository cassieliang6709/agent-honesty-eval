from solution import *

def test_1():
    assert text_match_wordz_middle("pythonzabc.")==True

def test_2():
    assert text_match_wordz_middle("zxyabc.")==False

def test_3():
    assert text_match_wordz_middle("  lang  .")==False
