def longest_substring_k_unique(s: str, k: int) -> int:
    if len(s) < 1 or len(s) > 1000000:
        return 0
    
    if k < 1 or k > len(s):
        return 0
    
    char_count = {}
    pointer1 = 0
    counter = 0

    for pointer2 in range(len(s)):
        char_count[s[pointer2]] = char_count.get(s[pointer2], 0) + 1

        while len(char_count) > k:
            char_count[s[pointer1]] -= 1
            if char_count[s[pointer1]] == 0:
                del char_count[s[pointer1]]
            pointer1 += 1
        
        if len(char_count) == k:
            counter = max(counter, pointer2 - pointer1 + 1)

    return counter

s = "araaci"
k = 2
print(longest_substring_k_unique(s, k))

s = "cbbebi"
k = 3
print(longest_substring_k_unique(s, k))

s = "aa"
k = 1
print(longest_substring_k_unique(s, k))