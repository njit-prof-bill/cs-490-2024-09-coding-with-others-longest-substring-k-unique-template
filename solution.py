def longest_substring_k_unique(s: str, k: int) -> int:
    n = len(s)
    answer = -1
    for i in range(n):
        for j in range(i+1, n+1):
            distinct = set(s[i:j])
            if len(distinct) == k:
                answer = max(answer, j - i)
    print(answer)

s = "aabbcc"
k = 3
 
# Function Call
longest_substring_k_unique(s,k)