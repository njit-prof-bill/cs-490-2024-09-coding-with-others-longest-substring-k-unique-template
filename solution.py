from collections import defaultdict
def longest_substring_k_unique(s: str, k: int) -> int:
    if k == 0:
        return 0

    # Dictionary to store the count of characters in current window
    char_count = defaultdict(int)
    left = 0
    max_len = 0
    unique_chars = 0

    for right in range(len(s)):
        # Include the current character in the window
        char_count[s[right]] += 1
        if char_count[s[right]] == 1:
            unique_chars += 1

        # Shrink the window from the left if more than k unique characters
        while unique_chars > k:
    for right in range(len(s)):
        # Include the current character in the window
        char_count[s[right]] += 1
        if char_count[s[right]] == 1:
            unique_chars += 1

        # Shrink the window from the left if more than k unique characters
        while unique_chars > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                unique_chars -= 1
            left += 1

        # If exactly k unique characters, update the maximum length
        if unique_chars == k:
            max_len = max(max_len, right - left + 1)

    return max_len if max_len > 0 else 0

s = "araaci"
k = 2
print(longest_substring_k_unique(s, k))  # Output: 4

s = "cbbebi"
k = 3
print(longest_substring_k_unique(s, k))  # Output: 5

s = "aa"
k = 1
print(longest_substring_k_unique(s, k))  # Output: 2
