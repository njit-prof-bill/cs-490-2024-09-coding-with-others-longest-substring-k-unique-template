def longest_substring_k_unique(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0
    
    char_count = {}
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        current_char = s[end]
        if current_char in char_count:
            char_count[current_char] += 1
        else:
            char_count[current_char] = 1
        
        while len(char_count) > k:
            start_char = s[start]
            char_count[start_char] -= 1
            if char_count[start_char] == 0:
                del char_count[start_char]
            start += 1
        
        if len(char_count) == k:
            max_length = max(max_length, end - start + 1)
    
    return max_length
