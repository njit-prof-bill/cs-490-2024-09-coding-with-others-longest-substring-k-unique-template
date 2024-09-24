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

        '''
        If the number of unique characters becomes greater than k, then our goal
        is to remove one of the unique characters from the set until the number of
        unique characters is equal to k again. This is done by shrinking the window
        from the left with the left pointer 'start'. But if we do this, we need to 
        ensure that the character that we just removed from the window doesn't have 
        duplicates currently still in the newly, shrunken window. If that is the case, 
        then we cannot remove the character from the set. This is why we are storing 
        the frequencies of each character in 'char_freq'. Once a character's frequency 
        reaches 0, only then can we remove it from the set.
        '''
        while len(unique) > k:
            char_idx = ord(s[start]) - ord('a') 
            char_freq[char_idx] -= 1
            
            if char_freq[char_idx] == 0:
                unique.remove(s[start])
            start += 1
        
        '''
        Only update 'max_len' when the number of unique characters equals to k.
        Otherwise, if that never happens, return max_len's initial value of 0.
        '''
        if len(unique) == k:
            curr_len = end - start + 1
            max_len = max(curr_len, max_len)

        end += 1

    return max_len

print(longest_substring_k_unique("araaci", 2))
print(longest_substring_k_unique("cbbebi", 3))
print(longest_substring_k_unique("aa", 1))
