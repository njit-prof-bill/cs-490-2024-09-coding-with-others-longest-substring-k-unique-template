def longest_substring_k_unique(s: str, k: int) -> int:
    n = len(s)
    max_length = -1

    for i in range(n):
        for j in range(i + 1, n + 1):

            char_set = set(s[i:j])
            if len(char_set) == k:
                max_length = max(max_length, j - i)

    return max_length
