from fuel import convert,gauge
import pytest

def test_convert():
    assert convert("4/5")==80
def test_gauge():
    assert gauge(1)=="E"
    assert gauge(99)=="F"
    assert gauge(70)=="70%"
def test_convert_error():
    with pytest.raises(ValueError):
        convert("5/4")
        convert("1.5/2")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
