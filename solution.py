def longest_substring_k_unique(s: str, k: int) -> int:
    if not s or k == 0:
        return 0

    count = {}
    left = 0
    maxLen = 0

    for right in range(len(s)):
        curr = s[right]
        count[curr] = count.get(curr, 0) + 1
        while len(count) > k:
            leftChar = s[left]
            count[leftChar] -= 1
            if count[leftChar] == 0:
                del count[leftChar]
            left += 1

        if len(count) == k:
            maxLen = max(maxLen, right - left + 1)

    if maxLen > 0:
        return maxLen
    else:
        pass
