def longest_substring_k_unique(s: str, k: int) -> int:
    n = len(s)
    ans = -1

    for i in range(n):
        for j in range(i+1, n+1):
            distinct = set(s[i:j])
            if len(distinct) == k:
                ans = max(ans, j - i)
                
    return ans

print(longest_substring_k_unique("araaci",2))
print(longest_substring_k_unique("cbbebi",3))
print(longest_substring_k_unique("aa",1))
    
