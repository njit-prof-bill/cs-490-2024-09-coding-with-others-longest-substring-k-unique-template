def longest_substring_k_unique(s: str, k: int) -> int:
    if len(s) == 0 or k == 0:
        return 0
    charFreq = {}
    left = 0
    maxLength = 0
    substrings = []
    for right in range(len(s)):
        rightChar = s[right]
        if rightChar not in charFreq:
            charFreq[rightChar] = 0
        charFreq[rightChar] += 1
        while len(charFreq) > k:
            leftChar = s[left]
            charFreq[leftChar] -= 1
            if charFreq[leftChar] == 0:
                del charFreq[leftChar]
            left += 1
        if len(charFreq) == k:
            currLength = right - left + 1
            currSubstring = s[left:right + 1]
            if currLength > maxLength:
                maxLength = currLength
                substrings = [currSubstring]  
            elif currLength == maxLength:
                substrings.append(currSubstring)
    if maxLength == 0:
        print(f'Input: S = "{s}", K = {k}')
        print(f'Output: 0')
        print(f'Explanation: No substring with exactly {k} unique characters.')
        return 0
    substringsOut = " or ".join(f'"{sub}"' for sub in substrings)
    print(f'Input: S = "{s}", K = {k}')
    print(f'Output: {maxLength}')
    print(f'Explanation: The longest substring with exactly {k} unique characters is {substringsOut}.')
    return maxLength
if __name__ == "__main__":
    s = input("Enter a string S: ")
    k = int(input("Enter a value K: "))
    longest_substring_k_unique(s, k)