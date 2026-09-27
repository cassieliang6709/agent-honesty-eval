from solution import *

def test_1():
    assert remove_uppercase('cAstyoUrFavoRitETVshoWs') == 'cstyoravoitshos'

def test_2():
    assert remove_uppercase('wAtchTheinTernEtrAdIo') == 'wtchheinerntrdo'

def test_3():
    assert remove_uppercase('VoicESeaRchAndreComMendaTionS') == 'oiceachndreomendaion'
