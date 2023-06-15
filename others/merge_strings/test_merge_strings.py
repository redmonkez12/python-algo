from others.merge_strings.merge_strings import merge_string


def test_merge_strings():
    word1 = "abc"
    word2 = "pqr"

    assert merge_string(word1, word2) == "apbqcr"

    word1 = "ab"
    word2 = "pqrs"

    assert merge_string(word1, word2) == "apbqrs"

    word1 = "abcd"
    word2 = "pq"

    assert merge_string(word1, word2) == "apbqcd"