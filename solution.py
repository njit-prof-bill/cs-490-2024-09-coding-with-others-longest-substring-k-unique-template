    
def longest_substring_k_unique(s: str, k: int) -> int:
    ans = -1
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            d = set(s[i:j])
            if (len(d) == k):
                ans = max(ans, j - i)
    print(ans)


longest_substring_k_unique("araaci",2)
longest_substring_k_unique("cbbebi",3)
longest_substring_k_unique("aaaaa",1)
longest_substring_k_unique("aabacbebebe", 3)
