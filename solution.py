def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    if len(s) == 0:
        return 0

    answer = 0
    left = 0
    right = left + 1
    unique_chars = {s[0]:1}

    while right < len(s):

        if unique_chars.get(s[right], 0) == 0:
            unique_chars[s[right]] = 1
            
        while len(unique_chars.keys()) > k:
            del unique_chars[s[left]]
            left += 1
        
        answer = max(right-left+1, answer)
        right += 1
        
    return answer

s = "aa"
k = 1

print(longest_substring_k_unique(s, k))