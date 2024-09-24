def longest_substring_k_unique(s: str, k: int) -> int:
    # containers for characters seen for iteration, string being compiled, and all strings compiled
    seenChars = []
    compiledStrings = []
    currentString = ""
    # nested loop that starts from first character and each iteration shrinks string by 1 length checking substrings
    for i in range(len(s)):
        for j in range(i,len(s)):
            # append characters not in seenChar array
            if s[j] not in seenChars:
                seenChars.append(s[j])
            # if the length of our seenChars array exceeds k break inner loop
            if len(seenChars) > k:
                break
            currentString = currentString + s[j]
        # append compiled string and clear other variables after break/end of string
        compiledStrings.append(currentString)
        currentString = ""
        seenChars = []

    # return max length of string from compiled string array
    maxLength = 0
    for i in range(len(compiledStrings)):
        if len(compiledStrings[i]) > maxLength:
            maxLength=len(compiledStrings[i])
    return maxLength    

# Tests
S = "araaci"
S2 = "cbbebi"
S3 = "aa"
S4 = "areeddci"

print(longest_substring_k_unique(S,2))
print(longest_substring_k_unique(S2,3))
print(longest_substring_k_unique(S3,1))
print(longest_substring_k_unique(S4,2))