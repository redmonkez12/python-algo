def merge_string(word1, word2):
    merged = ""
    i = 0
    j = 0

    while i < len(word1) and j < len(word2):
        merged += word1[i] + word2[j]
        i += 1
        j += 1

    merged += word1[i:]
    merged += word2[j:]

    return merged
