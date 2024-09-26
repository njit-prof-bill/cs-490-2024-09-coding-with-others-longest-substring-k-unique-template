def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    string = ''
    for i in range(len(s)): # Start at each character
        cList = []
        cList.append(s[i])
        for j in range(i+1, len(s)): # Start adding past the starting character
            if s[j] not in cList: # New character
                if len(cList) == k: # Adding new character would be too many
                    # Compare old string to new
                    if len(string) < len(s[i:j]): # New string is longer
                        string = s[i:j] # Set string to new string
                    break
                # Add new character to list
                cList.append(s[j])
    if len(string) == 0:
        string = s
    return len(string)

print(longest_substring_k_unique('araaci', 2))
print(longest_substring_k_unique('cbbebi', 3))
print(longest_substring_k_unique('aa', 1))