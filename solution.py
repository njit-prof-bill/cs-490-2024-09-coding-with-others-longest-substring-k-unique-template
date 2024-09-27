def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    if not s or k <= 0:
        return 0
    
    char_count = {} # create dictionary to keep count of each characters count
    start = 0 #start pointer
    max_length = 0
    unique_chars = 0 #find unique characters

    for end in range(len(s)):
        # Add the current character to the window
        if s[end] not in char_count:
            char_count[s[end]] = 0
            unique_chars += 1
        char_count[s[end]] += 1

        # Shrink the window if we have more than K unique characters
        while unique_chars > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
                unique_chars -= 1
            start += 1

        # Update max_length if we have exactly K unique characters
        if unique_chars == k:
            max_length = max(max_length, end - start + 1)

    return max_length
    
    
print(longest_substring_k_unique("araaci",2)) 
print(longest_substring_k_unique("cbbebi",3)) 
print(longest_substring_k_unique("aa",1)) 
print(longest_substring_k_unique("neel",2))
    
pass