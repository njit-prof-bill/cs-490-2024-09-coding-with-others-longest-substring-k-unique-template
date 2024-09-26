def longest_substring_k_unique(s: str, k: int) -> int:
    length = len(s)
    count = 0
    for i in range(length):
        for j in range(i+1, length+1):
            distinct = set(s[i:j])
            if len(distinct) == k:
                count = max(count, j - i)
    return count

# Test Cases
print(longest_substring_k_unique("araaci", 2))
print(longest_substring_k_unique("cbbebi", 3))
print(longest_substring_k_unique("aa", 1))
print(longest_substring_k_unique("araaciaar", 2))
print(longest_substring_k_unique("aa", 3))
print(longest_substring_k_unique("aa", 2))
print(longest_substring_k_unique("aaaaaaa", 2))
print(longest_substring_k_unique("aaaaaaabbbb", 4))
print(longest_substring_k_unique("aaaaaaabbbbcdaaaaaaaaaaaaaaa", 3))

            
            

