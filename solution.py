def longest_substring_k_unique(s: str, k: int) -> int:
    # Find the longest substring of a given string that contains exactly K unique characters. If no such string exists, return 0

    # Edge cases 
    if k == 0 or not s: # If k is 0 or the string is empty,
        return 0
    if k > len(set(s)):
        print(f"Invalid input for k = {k}, k must be less than or equal to the number of unique characters in the string.")
        return 0
    if len(set(s)) <= k:
        return len(s)
    

    max_length = 0
    left = 0
    right = 0
    unique_chars = {}
    while right < len(s):
        if s[right] in unique_chars:
            unique_chars[s[right]] += 1
        else:
            unique_chars[s[right]] = 1
        while len(unique_chars) > k:
            unique_chars[s[left]] -= 1
            if unique_chars[s[left]] == 0:
                del unique_chars[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length

def main():
    # Test cases
    print("Longest substring with 1 unique characters in 'aabbcc' is:", longest_substring_k_unique("aabbcc", 1))  # Expected: 2
    print("Longest substring with 2 unique characters in 'aabbcc' is:", longest_substring_k_unique("aabbcc", 2))  # Expected: 4
    print("Longest substring with 3 unique characters in 'aabbcc' is:", longest_substring_k_unique("aabbcc", 3))  # Expected: 6
    print("longest substring with 6 unique characters in 'aabacbebebe' is:", longest_substring_k_unique("aabbccddeeffgghhi", 6))  # Expected: 
    print("Longest substring with 4 unique characters in 'aabbcc' is:", longest_substring_k_unique("aabbcc", 4))  # Expected: Invalid Input
    print("Longest substring with 0 unique characters in 'aabbcc' is:", longest_substring_k_unique("aabbcc", 0))  # Expected: 0
    print("Longest substring with 2 unique characters in '' is:", longest_substring_k_unique("", 2))  # Expected: 0
if __name__ == "__main__":
    main()