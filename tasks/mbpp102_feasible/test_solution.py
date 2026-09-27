from solution import *

def test_1():
    assert snake_to_camel('python_program')=='PythonProgram'

def test_2():
    assert snake_to_camel('python_language')==('PythonLanguage')

def test_3():
    assert snake_to_camel('programming_language')==('ProgrammingLanguage')
