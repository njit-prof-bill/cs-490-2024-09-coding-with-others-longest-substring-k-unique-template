def longest_substring_k_unique(s: str, k: int) -> int:
    retCount = 0
    for i in range(len(s)):
        charCount = 0
        sub = ""
        #Check substring starting from i
        for j in range(i,len(s)):
            # when charCount is at limit and not in the substring
            if charCount == k and s[j] not in sub:
                break
            
            # when charCount is not at limit and not in substring
            elif charCount < k and s[j] not in sub:
                charCount +=1
                sub+=s[j]
            
            #when charCount maybe at limit but character is already there
            elif charCount<=k and s[j] in sub :
                sub += s[j]
        #if the substring is longer than current return count then we change
        if len(sub) > retCount:
            retCount = len(sub)
    return retCount
