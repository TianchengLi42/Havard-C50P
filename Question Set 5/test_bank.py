import pytest

from bank import value

def test_exception():
    with pytest.raises(AttributeError):
        value(1)

def test_upper():
    assert value('Hello') == 0
    assert value('HELLO') == 0
    assert value('HEY') == 20
    assert value("H") == 20
    assert value("HELL") == 20
    assert value("BIGGERISH") == 100

def test_lower():
    assert value('hello') == 0
    assert value('hey') == 20
    assert value("gibberish") == 100
 