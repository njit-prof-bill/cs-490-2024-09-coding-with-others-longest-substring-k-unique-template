
def longest_substring_k_unique(s: str, k: int) -> int:
    if k==0 or not s:
        return 0
    
    charCount={}
    left=0
    maxLength=0
    
    for right in range(len(s)):
        charCount[s[right]]=charCount.get(s[right], 0)+1
        
        while len(charCount)>k:
            charCount[s[left]]-=1
            
            if charCount[s[left]]==0:
                del charCount[s[left]]
                
            left+=1
        
        if len(charCount)==k:
            maxLength=max(maxLength, right-left+1)
    
    return maxLength

print(longest_substring_k_unique("ecexec", 2)) #Answer: 3
print(longest_substring_k_unique("ececx", 2)) #Answer: 4
print(longest_substring_k_unique("abaccc", 2)) #Answer: 4
print(longest_substring_k_unique("aaaaa", 1)) #Answer: 5
print(longest_substring_k_unique("abaccc", 0)) #Answer: 0
print(longest_substring_k_unique("aabacbebebe", 3)) #Answer: 7