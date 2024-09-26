def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    if len(s) == 0 or k > len(s) or k == 0:
        return 0

    answer = 1
    left = 0
    right = left + 1
    unique_chars = {s[0]:1}
    max_unique_chars = 1

    while right < len(s):

        if unique_chars.get(s[right], 0) == 0:
            unique_chars[s[right]] = 1
        else:
            unique_chars[s[right]] += 1

            
        while len(unique_chars.keys()) > k:
            unique_chars[s[left]] -= 1
            if unique_chars[s[left]] == 0:
                del unique_chars[s[left]]
            left += 1
        
        answer = max(right-left+1, answer)
        max_unique_chars = max(len(unique_chars.keys()), max_unique_chars)
        right += 1
        
    if max_unique_chars < k:
        answer = 0
        
    return answer

# Example test cases
print(longest_substring_k_unique("araaci", 2))  # Expected output: 4
print(longest_substring_k_unique("cbbebi", 3))  # Expected output: 5
print(longest_substring_k_unique("aa", 1))  # Expected output: 2

# Edge cases

# Case with no valid substrings
print(longest_substring_k_unique("abc", 4))  # Expected output: 0 (k > number of unique characters)

# Case with a string containing only one character repeated
print(longest_substring_k_unique("aaaaa", 1))  # Expected output: 5

# Case with `k = 1` and a string with all distinct characters
print(longest_substring_k_unique("abcdef", 1))  # Expected output: 1

# Case with `k = len(s)` (whole string should be the output)
print(longest_substring_k_unique("abcdef", 6))  # Expected output: 6

# Case with an empty string
print(longest_substring_k_unique("", 1))  # Expected output: 0 (since the string is empty)

# Case with `k = 0` (should return 0)
print(longest_substring_k_unique("abc", 0))  # Expected output: 0

# Case with large inputs
large_input = "a" * 10**6
print(longest_substring_k_unique(large_input, 1))  # Expected output: 1000000

# Case with all characters being the same and `k` > 1
print(longest_substring_k_unique("aaaaa", 2))  # Expected output: 0 (not enough unique characters)

# Case with minimum length string and maximum `k`
print(longest_substring_k_unique("a", 1))  # Expected output: 1

# Case where substring with exactly k unique characters is in the middle
print(longest_substring_k_unique("aabacbebebe", 3))  # Expected output: 7 ("cbebebe")
