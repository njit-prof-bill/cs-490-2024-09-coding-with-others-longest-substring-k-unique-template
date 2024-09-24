def longest_substring_k_unique(s: str, k: int) -> int:
    if k == 0 or k > len(set(s)):
        return 0
    
    maxSub = 0
    for i in range(len(s)):
        total = 1
        check = [s[i]]
        j = i + 1
        
        while j < len(s):
            if s[j] not in check:
                check.append(s[j]) 
                total += 1
                if total > k:
                    break
            j += 1
        maxSub = max(maxSub, j - i)

    return maxSub if maxSub > 0 else 0
    

print(longest_substring_k_unique("araaci", 2))
print(longest_substring_k_unique("cbbebi", 3))
print(longest_substring_k_unique("aa", 1))
