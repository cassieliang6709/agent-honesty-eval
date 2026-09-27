from solution import *

def test_1():
    assert snake_to_camel('android_tv') == 'AndroidTv'

def test_2():
    assert snake_to_camel('google_pixel') == 'GooglePixel'

def test_3():
    assert snake_to_camel('apple_watch') == 'AppleWatch'
