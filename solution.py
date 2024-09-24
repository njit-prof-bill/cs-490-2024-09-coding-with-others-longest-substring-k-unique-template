def longest_substring_k_unique(s: str, k: int) -> int:
    length = len(s)
    max_l = 0
    for i in range(length):
        for j in range(i + 1, length + 1):
            curr = set(s[i:j])
            if len(curr) == k:
                max_l = max(max_l, j - i)
    return max_l

print(longest_substring_k_unique("araaci", 2))
print(longest_substring_k_unique("cbbebi", 3))
print(longest_substring_k_unique("aa", 1))

