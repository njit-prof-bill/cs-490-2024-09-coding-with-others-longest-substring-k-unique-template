def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    stack = []
    found = {}
    currK = 0
    substringCount = 0
    for x in s[::-1]:
        stack.append(x)
    
    while stack:
        character = stack.pop()
        if found.get(character,None):
            pass
        else:
            currK+=1
            found[character] = True
        if currK>k:
            return substringCount
        substringCount +=1
    return substringCount

print(longest_substring_k_unique("araaci",2))
print(longest_substring_k_unique("cbbebi",3))
print(longest_substring_k_unique("aa",1))
