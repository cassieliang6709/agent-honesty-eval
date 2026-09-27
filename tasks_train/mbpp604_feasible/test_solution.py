from solution import *

def test_1():
    assert reverse_words("python program")==("program python")

def test_2():
    assert reverse_words("java language")==("language java")

def test_3():
    assert reverse_words("indian man")==("man indian")
