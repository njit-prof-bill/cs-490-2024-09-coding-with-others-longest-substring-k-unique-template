def longest_substring_k_unique(s: str, k: int) -> int:
    character_count = {}
    n = len(s)
    left = 0
    solution = -1
    if n == 0 or k == 0:
        return -1
    for right in range(n):
        character_count[s[right]] = character_count.get(s[right], 0) + 1
        while len(character_count) > k:
            character_count[s[left]] = character_count[s[left]] - 1
            if character_count[s[left]] == 0:
                del character_count[s[left]]
            left = left + 1
        if len(character_count) == k:
            solution = max(solution, right - left + 1)
    print(solution)
    return solution