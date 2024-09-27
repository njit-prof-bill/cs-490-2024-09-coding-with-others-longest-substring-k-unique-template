def longest_substring_k_unique(s: str, k: int) -> int:
    #Write your code here
    pass

    start = 0
    max_length = 0
    char_freq = {}

    right = 0
    while right < len(s):
        current_char = s[right]
        char_freq[current_char] = char_freq.get(current_char, 0) + 1
        while len(char_freq) > k:
            char_start = s[start]  
            char_freq[char_start] -= 1  
            if char_freq[char_start] == 0:
                del char_freq[char_start]
            start += 1
        if len(char_freq) == k:
            max_length = max(max_length, right - start + 1)

        right += 1
    return max_length

print(longest_substring_k_unique("araaci", 2))  # Output: 4
print(longest_substring_k_unique("cbbebi", 3))  # Output: 5
print(longest_substring_k_unique("aa", 1))      # Output: 2