def find_the_difference(s, t):
    # s_sum = 0
    # t_sum = 0
    #
    # for char in s:
    #     s_sum += ord(char)
    #
    # for char in t:
    #     t_sum += ord(char)
    #
    # return chr(t_sum - s_sum)

    x = 0
    for c in s + t:
        x ^= ord(c)

    return chr(x)

