def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    subset = {} #Dictionary that stores the elements until the given subset length
    j = 0
    count = 0
    for i in range(len(s)):
        subset[s[i]] = subset.get(s[i], 0) + 1 #Adds the 
        while len(subset) > k:
            subset[s[j]] -= 1
            if subset[s[j]] == 0:
                del subset[s[j]]
            j += 1
        count = max(count, i - j + 1)
    return count
    pass
