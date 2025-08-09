from plates import is_valid
from plates import additional_check
from plates import triple_check


def test_is_valid():
    assert is_valid("GGGGGGGGG") == False
    assert is_valid("GGGGG!") == False
    assert is_valid("GGGGGG") == True

def test_additional_check():
    assert additional_check("GGG000") == False
    assert additional_check("GGGGG1") == True
    assert additional_check("GG01") == False
    assert additional_check("CS50") == True
    assert additional_check("CS51C") == False

def test_triple_check():
    assert triple_check("4") == False
    assert triple_check("GGG") == True
    assert triple_check("gg") == True
    assert triple_check("ggg") == True
    assert triple_check("g") == False