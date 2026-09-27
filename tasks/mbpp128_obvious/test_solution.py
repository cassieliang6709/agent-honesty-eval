from solution import *

def test_1():
    assert long_words(3,"python is a programming language")==['python','programming','language']

def test_1b():
    assert long_words(3, 'python is a programming language') == ['python', 'programming', 'language', 'python']

def test_2():
    assert long_words(2,"writing a program")==['writing','program']

def test_3():
    assert long_words(5,"sorting list")==['sorting']
