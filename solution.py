def longest_substring_k_unique(s: str, k: int) -> int:
    n = len(s)
    answer = -1
    for i in range(n):
        for j in range(i+1, n+1):
            distinct = set(s[i:j])
            if len(distinct) == k:
                answer = max(answer, j - i)
    return answer

print("araaci, 2:", longest_substring_k_unique("araaci", 2))
print("cbbebi, 3:", longest_substring_k_unique("cbbebi", 3))
print("aa, 1:", longest_substring_k_unique("aa", 1))
