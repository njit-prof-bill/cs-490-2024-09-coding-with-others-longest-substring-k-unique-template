def longest_substring_k_unique(s: str, k: int) -> int:
    subset = {} #Dictionary that stores the frequency of letters in order to keep track of unique letters
    j = 0
    count = 0 #Stores the length of the longest substring with k unique characters
    for i in range(len(s)):
        subset[s[i]] = subset.get(s[i], 0) + 1 #Check if letter is included in dictionary. If yes, return the frequency and add 1. Else, just add 1
        while len(subset) > k: #Once the number of unique letters exceed the value of k, start removing letters
            subset[s[j]] -= 1 #Reduces the frequency of a letter to accomondate the new unique letter until one is removed
            if subset[s[j]] == 0: 
                del subset[s[j]] #If the frequency of the letter becomes 0, remove the letter itself to add new unique letter
            j += 1 #Traverses through the dictionary as long as there are more unique letters than required
        count = max(count, i - j + 1) #Compares the value of count with the value of the difference between iterated string length (i) and remove characters to maintain k unique variables (j) added by 1 (because index starts with 0)
    return count
    pass
