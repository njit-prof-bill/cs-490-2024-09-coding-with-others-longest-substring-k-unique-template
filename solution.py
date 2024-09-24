def longest_substring_k_unique(s: str, k: int) -> int:
    maxlen = -1
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            if (len(set(s[start:end])) == k):
                maxlen = max(maxlen, end-start)
    return(maxlen)
    pass
