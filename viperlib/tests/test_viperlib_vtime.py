from viperlib.src.vtime import *

def test_secs2time():
    assert secs2time(0) == '00:00:00'
    assert secs2time(1) == '00:00:01'
    assert secs2time(100) == '00:01:40'
    assert secs2time(1000) == '00:16:40'
    assert secs2time(999) == '00:16:39'
    assert secs2time(3600) == '01:00:00'
