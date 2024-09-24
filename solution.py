def longest_substring_k_unique(s: str, k: int) -> int:
    if k == 0 or k > len(s):  
        return 0

    left, max_length = 0, 0
    char_count = {}  

    for right in range(len(s)):  
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        if len(char_count) == k:
            max_length = max(max_length, right - left + 1)

    return max_length

