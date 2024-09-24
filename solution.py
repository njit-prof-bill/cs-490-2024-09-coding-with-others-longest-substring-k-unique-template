def longest_substring_k_unique(s: str, k: int) -> int:
    
    longest = 0

    if (len(s)==1):
        return 1
    
    if (len(s)==2):
        if(len(set(s)) == 1):
            return 2
        else:
            return 1

    beg=0
    end=1

    while (end<len(s) and beg<len(s)):
        myStr = s[beg:end]
        unq = len(set(myStr))
        if (unq<=k):
            if ((end-beg)>longest):
                longest = end-beg
            end+=1
            
        else:
            beg+=1
    return longest


#test cases

print(longest_substring_k_unique('araaci',2)) # outputs 4
print(longest_substring_k_unique('cbbebi',3)) # outputs 5
print(longest_substring_k_unique('aa',1)) # outputs 2