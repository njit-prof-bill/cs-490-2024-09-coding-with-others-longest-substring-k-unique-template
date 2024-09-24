def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    if(len(s) >= 1 and (k >= 1 and k < len(s))):
        max = 0
        for i in range(len(s)):
            substr = ""
            val = 0
            for j in range(i, len(s)):
                if(s[j] not in substr):
                    if(val == k):
                        break
                    if(val < k):
                        val+=1
                        substr += s[j]
                elif(s[j] in substr):
                    if(val <= k):
                        substr += s[j]
            if(len(substr) > max):
                max = len(substr)
    return max