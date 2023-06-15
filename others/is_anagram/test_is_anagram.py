from others.is_anagram.is_anagram import is_anagram


def test_is_anagram():
    s = "anagram"
    t = "nagaram"

    assert is_anagram(s, t) == True

    s = "rat"
    t = "car"

    assert is_anagram(s, t) == False
