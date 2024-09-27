def longest_substring_k_unique(s: str, k: int) -> int:
    
    # if no string is given or k is 0, exit out
    if not s or k == 0:
        return 0

    # Dictionary to store the frequency of characters in the current window
    char_freq = {}

    # Neccesary variables for sliding window Initialization
    left_pointer = 0
    max_len = 0 #

    #looping throught he string
    for right_pointer in range(len(s)):
        # Add the character at the right pointer to the dictionary (or update it's frequency)
        char_freq[s[right_pointer]] = char_freq.get(s[right_pointer], 0) + 1

        #while the number of unique characters is greater than k, shrink the window
        while len(char_freq) > k:
            # decrease tje frequency of the character at the left_pointer
            char_freq[s[left_pointer]] -= 1

            # if the frequency becomes 0, remove it from the dictionary
            if char_freq[s[left_pointer]] == 0:
                del char_freq[s[left_pointer]]
            
            # move the left_pointer to the right
            left_pointer += 1
        
        # update the max_len if the current window length is larger
        max_len = max(max_len, right_pointer - left_pointer + 1)

    return max_len

# Test Cases
#Hw provided test cases
print("Hw page provided test cases: ")
S = "araaci"
K = 2
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 4
print("Explanation: The longest substring with exactly 2 unique characters is 'araa'.\n")

# New Case 15: Input: S = "cbbebi", K = 3
S = "cbbebi"
K = 3
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 5
print("Explanation: The longest substring with exactly 3 unique characters is 'cbbeb' or 'bbebi'.\n")

# New Case 16: Input: S = "aa", K = 1
S = "aa"
K = 1
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 2
print("Explanation: The longest substring with exactly 1 unique character is 'aa'.\n")
print()

# Extra Test Cases:
print("Extra Test Cases:")
# Case 1: Single character string with K = 1
S = "a"
K = 1
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 1
print("Explanation: The longest substring with exactly 1 unique character is 'a'.\n")

# Case 2: All characters are unique, and K = length of the string
S = "abcdef"
K = 6
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 6
print("Explanation: The longest substring with exactly 6 unique characters is 'abcdef'.\n")

# Case 3: All characters are the same, K = 1
S = "aaaaa"
K = 1
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 5
print("Explanation: The longest substring with exactly 1 unique character is 'aaaaa'.\n")

# Case 4: Repeated characters with a reasonable value of K
S = "aabbcc"
K = 2
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 4 (e.g., "aabb" or "bbcc")
print("Explanation: The longest substring with exactly 2 unique characters can be 'aabb' or 'bbcc'.\n")

# Case 5: String with exactly K unique characters
S = "abcabcabc"
K = 3
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 9
print("Explanation: The longest substring with exactly 3 unique characters is 'abcabcabc'.\n")

# Case 6: K is larger than the number of distinct characters in the string
S = "ab"
K = 3
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 0
print("Explanation: There are not enough unique characters in the string to meet K.\n")

# Case 7: Substring with exactly K unique characters
S = "abcba"
K = 2
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 3
print("Explanation: The longest substring with exactly 2 unique characters is 'bcb'.\n")

# Case 8: Empty string
S = ""
K = 1
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 0
print("Explanation: The input string is empty.\n")

# Case 9: Large string with repeated patterns
large_string = "abababababababababababababababababababababab"
K = 2
print("Input: S =", large_string, ", K =", K)  
print("Output:", longest_substring_k_unique(large_string, K))  # Expected output: 44
print("Explanation: The longest substring with exactly 2 unique characters is the entire string.\n")

# Case 10: String with special characters and K = 3
S = "a@b!a@b!c"
K = 3
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 9
print("Explanation: The longest substring with exactly 3 unique characters is 'a@b!a@b!c'.\n")

# Case 11: Very large string with a single repeated character
large_string_single_char = "a" * 10**6
K = 1
print("Input: S = aaaa(10^6 times)", ", K =", K)  
print("Output:", longest_substring_k_unique(large_string_single_char, K))  # Expected output: 1000000
print("Explanation: The longest substring with exactly 1 unique character is the entire string.\n")

# Case 12: String with both letters and numbers, K = 3
S = "abc123abc123"
K = 3
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 6
print("Explanation: The longest substring with exactly 3 unique characters can be 'abc' or '123'.\n")

# Case 13: String with only symbols and K = 2
S = "!!!@@@###"
K = 2
print("Input: S =", S, ", K =", K)  
print("Output:", longest_substring_k_unique(S, K))  # Expected output: 6
print("Explanation: The longest substring with exactly 2 unique characters can be '!!!@@@'.\n")













