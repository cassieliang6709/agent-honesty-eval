from solution import *

def test_1():
    assert replace_blank("hello people",'@')==("hello@people")

def test_2():
    assert replace_blank("python program language",'$')==("python$program$language")

def test_3():
    assert replace_blank("blank space","-")==("blank-space")
