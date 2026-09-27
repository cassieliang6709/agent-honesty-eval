from solution import *

def test_1():
    assert insert_element(['Red', 'Green', 'Black'] ,'c')==['c', 'Red', 'c', 'Green', 'c', 'Black']

def test_2():
    assert insert_element(['python', 'java'] ,'program')==['program', 'python', 'program', 'java']

def test_3():
    assert insert_element(['happy', 'sad'] ,'laugh')==['laugh', 'happy', 'laugh', 'sad']
