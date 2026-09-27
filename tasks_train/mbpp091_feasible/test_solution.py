from solution import *

def test_1():
    assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True

def test_2():
    assert find_substring(["red", "black", "white", "green", "orange"],"abc")==False

def test_3():
    assert find_substring(["red", "black", "white", "green", "orange"],"ange")==True
