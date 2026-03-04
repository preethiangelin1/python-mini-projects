from caeser_cipher import encrypt, decrypt

def test_encrypt():
    assert encrypt("abc", 1) == "bcd"
    assert encrypt("abc", 0) == "abc"
    assert encrypt("", 5) == ""

def test_decrypt():
    assert decrypt("bcd", 1) == "abc"
    assert decrypt("bcd", 0) == "bcd"
    assert decrypt("", 5) == ""