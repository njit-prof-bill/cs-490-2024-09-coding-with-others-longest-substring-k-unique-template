def longest_substring_k_unique(s: str, k: int) -> int:
    
    letter = []
    maxLen = 0
    currentIndex = 0
    endIndex = 0

    if k > len(s) or len(s) == 0:
        return 0
    
    for char in s:
        bChar = char in letter
        inRangeForAdd = len(letter) != k

        if not bChar and inRangeForAdd:
            letter.append(char)
        elif not inRangeForAdd and not bChar:
            endIndex = currentIndex
            break
            
        currentIndex += 1
    

    if endIndex == 0:#if end was reached
        maxLen = currentIndex
    else:
        maxLen = endIndex

    if len(letter) < k:#if max len found was less than k
        maxLen = 0
    
    #find subsequent patterns
    nextMaxLen = longest_substring_k_unique(s[1:], k)
    
    if (maxLen < nextMaxLen):
        return nextMaxLen
   
    return maxLen

print(longest_substring_k_unique("araaci", 2))
print(longest_substring_k_unique("cbbebi", 3))
print(longest_substring_k_unique("aa", 1))
print(longest_substring_k_unique("araa", 3))