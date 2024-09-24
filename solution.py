def longest_substring_k_unique(s: str, k: int) -> int:
    
    letter = []

    if k > len(s) or len(s) == 0:
        return 0
    
    maxLen = 0

    currentIndex = 0
    endIndex = 0

    for char in s:

        bChar = char in letter
        inRangeForAdd = len(letter) != k

        if not bChar and inRangeForAdd:
            letter.append(char)
        elif not inRangeForAdd and not bChar:
            endIndex = currentIndex
            break
            
        currentIndex += 1
    
    if endIndex == 0:
        return currentIndex
    
    maxLen = endIndex
    
    nextMaxLen = longest_substring_k_unique(s[1:], k)
    
    if (maxLen < nextMaxLen):
        return nextMaxLen
   
    return maxLen



print(longest_substring_k_unique("araaci", 2))
print(longest_substring_k_unique("cbbebi", 3))
print(longest_substring_k_unique("aa", 1))