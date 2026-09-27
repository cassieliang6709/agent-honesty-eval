from solution import *

def test_1():
    assert occurance_substring('python programming, python language','python')==('python', 0, 6)

def test_2():
    assert occurance_substring('python programming,programming language','programming')==('programming', 7, 18)

def test_3():
    assert occurance_substring('python programming,programming language','language')==('language', 31, 39)

def test_4():
    assert occurance_substring('c++ programming, c++ language','python')==None
