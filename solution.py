def longest_substring_k_unique(s: str, k: int) -> int:
        if k == 0 or not s:
        return 0

    left = 0
    maxLen = 0
    charCount = {}

    for i in range(len(s)):
        char = s[i]
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

        while len(charCount) > k:
            leftChar = s[left]
            charCount[leftChar] -= 1
            if charCount[leftChar] == 0:
                del charCount[leftChar]
            left += 1

        if len(charCount) == k:
            maxLen = max(maxLen, i - left + 1)

    return maxLen
    pass
