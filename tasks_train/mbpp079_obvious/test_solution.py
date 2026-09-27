from solution import *

def test_1():
    assert word_len("Hadoop") == False

def test_1b():
    assert word_len('Hadoop') == True

def test_2():
    assert word_len("great") == True

def test_3():
    assert word_len("structure") == True
