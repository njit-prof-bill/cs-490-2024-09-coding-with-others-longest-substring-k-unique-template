def longest_substring_k_unique(s: str, k: int) -> int:
    if len(set(s)) < k:
        return 0
    count = {}
    maxLength = 0
    left = 0 
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1

        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]] 
            left += 1
        if len(count) == k:
            maxLength = max(maxLength, right - left + 1)
    
    return maxLength
