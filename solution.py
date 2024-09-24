from collections import defaultdict

def longest_substring_k_unique(s: str, k: int) -> int:
    if k == 0:
        return 0

    char_count = defaultdict(int) # Store frequency of chars
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] += 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1  # Move the left pointer

        if len(char_count) == k: # Update maximum length
            max_length = max(max_length, right - left + 1)

    return max_length

print("Testcase 1:", longest_substring_k_unique("araaci", 2)) # Expected output: 4
print("Testcase 2:", longest_substring_k_unique("cbbebi", 3)) # Expected output: 5
print("Testcase 3:", longest_substring_k_unique("aa", 1)) # Expected output: 2
print("Testcase 4:", longest_substring_k_unique("abcdef", 0)) # Expected output: 0
print("Testcase 5:", longest_substring_k_unique("aabbcc", 3)) # Expected output: 6
print("Testcase 6:", longest_substring_k_unique("abcdef", 7)) # Expected output: 0
