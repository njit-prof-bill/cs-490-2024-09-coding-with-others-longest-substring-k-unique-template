def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    dict = {}
    res = 0
    uniquecount=0
    l=0
    r=-1
    for i in s:
        r+=1
        if i not in dict or dict[i]==0:
            dict[i]=1
            uniquecount+=1
        else:
            dict[i]+=1
        while uniquecount>k:
            dict[s[l]]-=1
            if dict[s[l]]==0:
                uniquecount-=1
            l+=1

        if k == uniquecount:
            res = max(res, r-l+1)
    return res

