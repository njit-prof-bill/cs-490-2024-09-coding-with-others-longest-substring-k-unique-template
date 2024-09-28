def longest_substring_k_unique(s: str, k: int) -> int:
#Jhanvi Pai - CS490
#best case - there is no unique characters to be found
    if k == 0:
        return 0
    
    # Dictionary to store the count of unique characters in the current window
    char_count = {}
    max_len = 0
    left = 0

    # Expand the window with the right pointer to explore string
    for right in range(len(s)):
        char = s[right]
        #updating frequency count of current character
        char_count[char] = char_count.get(char, 0) + 1

        # If the window has more than K unique characters, shrink it from the left
        while len(char_count) > k:
            left_char = s[left]
            #reduces character count of leftmost character
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                #remove character from window
                del char_count[left_char]
            #move left point one step to right
            left += 1

        # Check if the current window has exactly K unique characters
        if len(char_count) == k:
            max_len = max(max_len, right - left + 1)

    return max_len if max_len > 0 else 0


#Test case 1 - normal case
s = "araaci"
k = 2
print("Length of longest substring is: ")
print(longest_substring_k_unique(s, k))  # Output: 4


#Test case 2 - normal case long answer
s = "aabacbebebe"
k = 3
print("Length of longest substring is: ")
print(longest_substring_k_unique(s, k))  # Output: 7

#Test case 3 - K is the number of distinct characters in string
s = "abcabcabc"
k = 3
print("Length of longest substring is: ")
print(longest_substring_k_unique(s, k))  # Output: 9

#Test case 4 - string with one character
s = "a"
k = 1
print("Length of longest substring is: ")
print(longest_substring_k_unique(s, k))  # Output: 1

#Test case 5 - max length string edge case
s = "a" * (10**6)
k = 1
print("Length of longest substring is: ")
print(longest_substring_k_unique(s, k))  # Output: 10**6

#Test case 6 - multiple substrings of same length
s = "abaccc"
k = 2
print("Length of longest substring is: ")
print(longest_substring_k_unique(s, k))  # Output: 4
