def longest_substring_k_unique(s: str, k: int) -> int:
    left = 0
    retLength = 0
    charMap = {}
    for right in range(len(s)):
        rightChar = s[right]
        charMap[rightChar] = charMap.get(rightChar, 0) + 1
        while len(charMap) > k:
            leftChar = s[left]
            charMap[leftChar] -= 1
            if charMap[leftChar] == 0:
                del charMap[leftChar]
            left += 1
        retLength = max(retLength, right - left + 1)
    return retLength
s = "araaci" 
k = 2
print(longest_substring_k_unique(s,k)) #4

s = "cbbebi" 
k = 3
print(longest_substring_k_unique(s,k)) #5

s = "aa" 
k = 1
print(longest_substring_k_unique(s,k)) #2
