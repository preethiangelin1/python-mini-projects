from main import has_user_won

def test_has_user_won():
    assert has_user_won(["_", "_", "l", "l", "_"]) == False
    assert has_user_won(["h", "e", "l", "l", "o"]) == True