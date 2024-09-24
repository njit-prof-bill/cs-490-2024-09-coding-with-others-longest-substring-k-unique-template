def longest_substring_k_unique(s: str, k: int) -> int:
    if len(s) == 0 or k == 0 or k > len(s):
        return 0
    
    max_len = 0

    # sliding window with two pointers 'start' and 'end'
    start, end = 0, 0

    # a set to store unique characters
    unique = set()

    # array to store frequencies of each character
    char_freq = [0] * 26 

    while end < len(s):
        # add unique char to the set 
        unique.add(s[end])

        # index of the char in the char_freq array
        char_idx = ord(s[end]) - ord('a')

        # update the char's frequency
        char_freq[char_idx] += 1

        while len(unique) > k:
            char_idx = ord(s[start]) - ord('a') 
            char_freq[char_idx] -= 1
            
            if char_freq[char_idx] == 0:
                unique.remove(s[start])
            start += 1
        
        if len(unique) == k:
            curr_len = end - start + 1
            max_len = max(curr_len, max_len)

        end += 1

    return max_len

print(longest_substring_k_unique("araaci", 2))
print(longest_substring_k_unique("cbbebi", 3))
print(longest_substring_k_unique("aa", 1))
