import pytest

from fuel import convert
from fuel import gauge

def test_convert_value():
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("1/4") == 25

def test_convert_exceptions():
    with pytest.raises(ValueError):
        convert("A/B")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("5/4")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"

