import pytest

from twttr import shorten

def test_shorten_lower():
    assert shorten("tian") == "tn"

def test_shorten_upper():
    assert shorten("TIAN") == "TN"

def test_shorten_exception():
    with pytest.raises(TypeError):
        shorten(2)