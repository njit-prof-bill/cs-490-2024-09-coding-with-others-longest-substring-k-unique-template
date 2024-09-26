def longest_substring_k_unique(s: str, k: int) -> int:
    if len(s) == 0 or k == 0 or k > len(s):
        return 0

    start = 0
    max_length = 0
    char_count = {}

    for end in range(len(s)):
        current_char = s[end]
        if current_char in char_count:
            char_count[current_char] += 1
        else:
            char_count[current_char] = 1

        while len(char_count) > k:
            left_char = s[start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            start += 1

        if len(char_count) == k:
            current_length = end - start + 1
            if current_length > max_length:
                max_length = current_length

    return max_length

print(longest_substring_k_unique("araaci", 2))
print(longest_substring_k_unique("cbbebi", 3))
print(longest_substring_k_unique("aa", 1))
