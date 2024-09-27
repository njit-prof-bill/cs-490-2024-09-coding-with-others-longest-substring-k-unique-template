def longest_substring_k_unique(s: str, k: int) -> int:
    length = len(s)
    if length == 0 or k == 0 or length < k:
        return 0
    max_length = 0
    for i in range(length):
        unique_chars = set()
        for j in range(i, length):
            unique_chars.add(s[j])
            if len(unique_chars) == k:
                current_length = j - i + 1
                max_length = max_length if max_length > current_length else current_length
            elif len(unique_chars) > k:
                break
    return max_length


assert longest_substring_k_unique('', 0) == 0
assert longest_substring_k_unique('', 10) == 0

assert longest_substring_k_unique('aaaaabbbdfsdg', 1) == 5

assert longest_substring_k_unique('aaaaabbbdfsdg', 10) == 0

assert longest_substring_k_unique('araaci', 2) == 4
assert longest_substring_k_unique('cbbebi', 3) == 5
assert longest_substring_k_unique('abababc', 3) == 7
