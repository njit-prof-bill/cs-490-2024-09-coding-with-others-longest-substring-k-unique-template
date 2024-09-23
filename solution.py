from collections import defaultdict

def longest_substring_k_unique(s: str, k: int) -> int:
    seen = defaultdict(int)
    left = right = 0
    window = 0
    while right < len(s) and k > 0:
        if s[right] not in seen and len(seen.keys()) >= k:
            while seen[s[left]] > 1:
                seen[s[left]] -= 1
                left += 1
            del seen[s[left]]
            left += 1
        seen[s[right]] += 1

        window = max(window, right - left + 1)
        right += 1
    return window
print(longest_substring_k_unique('aaaarrrr', 2))