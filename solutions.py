def longest_substring_k_unique(s: str, k: int) -> int:
    '''
    If string is empty, return 0
    Integer default should be 0 otherwise
    Min Window size is K, string length must be min K long to count...
    but start with window size = to length of string. That way we can return immediately if conditions met (only K unique chars)
    If we get to min window size and there are not K unique chars...return 0.

    Will require sliding window?
    '''

    win_size = len(s)
    str_len = len(s)
    while win_size != 0:
        for j in range(0, str_len - win_size + 1, 1):
            new_str = s[j:j+win_size]
            set_size = len(set(new_str))
            if set_size == k:
                print(len(new_str))
                return len(new_str)
        win_size -= 1
    return 0

longest_substring_k_unique("aa", 1)
