from solution import *

def test_1():
    assert add_string([1,2,3,4],'temp{0}')==['temp1', 'temp2', 'temp3', 'temp4']

def test_2():
    assert add_string(['a','b','c','d'], 'python{0}')==[ 'pythona', 'pythonb', 'pythonc', 'pythond']

def test_3():
    assert add_string([5,6,7,8],'string{0}')==['string5', 'string6', 'string7', 'string8']
