from solution import *

def test_1():
    assert remove_all_spaces('python  program')==('pythonprogram')

def test_2():
    assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')

def test_3():
    assert remove_all_spaces('python                     program')==('pythonprogram')

def test_4():
    assert remove_all_spaces('   python                     program')=='pythonprogram'
