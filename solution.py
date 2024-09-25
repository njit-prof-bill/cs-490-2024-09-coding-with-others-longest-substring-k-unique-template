def longest_substring_k_unique(s: str, k: int) -> int:
    n = len(s)
    output = -1
    
    for i in range(n):
        for j in range(i+1, n+1):
            unique_nums = set(s[i:j])
            
            if len(unique_nums) == k:
                output = max(output, j-i)
                
    print("Output:", output)            
    pass

#test cases
#longest_substring_k_unique("cbbebi", 3)
