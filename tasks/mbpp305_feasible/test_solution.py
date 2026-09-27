from solution import *

def test_1():
    assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')

def test_2():
    assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')

def test_3():
    assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')
