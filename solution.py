def longest_substring_k_unique(s: str, k: int) -> int:

    if k == 0 or s is None:
        return 0
    
    n = len(s)  
    result = 0 
    
    for left in range(n):   
        for right in range(left + 1, n + 1):  
            distinct_chars = set(s[left:right])
            if len(distinct_chars) == k:
                result = max(result, right - left)
    
    return result

longest_substring_k_unique("cbebbi", 3)
