def longest_substring_k_unique(s: str, k: int) -> int:
    if k == 0:
        return 0
    
    # Dictionary to store the frequency of characters in the current window
    char_count = {}
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        # Add the current character to the dictionary or update its count
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # If the number of unique characters exceeds k, shrink the window
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # If we have exactly k unique characters, update the max_length
        if len(char_count) == k:
            max_length = max(max_length, right - left + 1)
    
    return max_length if max_length > 0 else 0

def main():
    print(longest_substring_k_unique("aabbcc", 2))  # Expected output: 4 ("aabb" or "bbcc")
    print(longest_substring_k_unique("aabbcc", 1))  # Expected output: 2 ("aa", "bb", or "cc")
    print(longest_substring_k_unique("aaabbb", 3))  # Expected output: 0 (no substring with exactly 3 unique chars)
    print(longest_substring_k_unique("abcba", 2))   # Expected output: 3 ("bcb")
    print(longest_substring_k_unique("", 2))        # Expected output: 0 (empty string)


if __name__ == "__main__":
    main()
