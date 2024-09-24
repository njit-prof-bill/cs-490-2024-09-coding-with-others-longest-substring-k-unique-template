def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    d = {}
    res = 0
    
    curr_unique_ct=0
    lp=0
    rp=-1
    for i in s:
        rp+=1
        if i not in d or d[i]==0:
            d[i]=1
            curr_unique_ct+=1
        else:
            d[i]+=1
        # print(lp,rp, d, curr_unique_ct)

        while curr_unique_ct>k:
            lchar = s[lp]
            d[lchar]-=1
            if d[lchar]==0:
                curr_unique_ct-=1
            lp+=1

        if curr_unique_ct == k:
            res = max(res, rp-lp+1)
            
    return res