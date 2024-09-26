def longest_substring_k_unique(s: str, k: int) -> int:
    """Function that finds the longest substring of a given string that contains exactly k unique characters.
    If no such substring exists, return 0.

    Args:
        s (str): A string between 1 and 10^6 char.
        k (int): Integer between 1 and number of unique char in s.

    Returns:
        int: Length of the substring in the given string.
    """
    
    # Case to handle if an empty string is somehow passed or k is 0
    if k == 0 or not s:
        return 0

    start = 0
    max_length = 0
    char_count = {}

    for end in range(len(s)):
        char_count[s[end]] = char_count.get(s[end], 0) + 1

        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1

        if len(char_count) == k:
            max_length = max(max_length, end - start + 1)

    return max_length

# Example usage:
print(longest_substring_k_unique("araaci", 2))  # Output: 4
print(longest_substring_k_unique("cbbebi", 3))  # Output: 5
print(longest_substring_k_unique("aa", 1))      # Output: 2

