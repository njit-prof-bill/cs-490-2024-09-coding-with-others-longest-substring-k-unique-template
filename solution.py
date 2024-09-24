def longest_substring_k_unique(s: str, k: int) -> int:
    n = len(s)
    answer = -1
    for i in range(n):
        for j in range(i + 1, n +1):
            distinct = set(s[i:j])
            if len(distinct) == k:
                answer = max(answer, j - i)
    print(answer)

S = 'araaci'
K = 2
longest_substring_k_unique(S, K)
print()

S = 'cbbebi'
K = 3
longest_substring_k_unique(S, K)
print()

S = 'aa'
K = 1
longest_substring_k_unique(S, K)
