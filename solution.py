def longest_substring_k_unique(s: str, k: int) -> int:
    ans = 0
    n = len(s)

    for i in range(n):
        for j in range(i+1, n+1):
            substring = set(s[i:j])
            if len(substring) == k:
                ans = max(ans, j-i)
    return ans
