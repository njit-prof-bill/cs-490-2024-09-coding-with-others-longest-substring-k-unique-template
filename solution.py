'''
Write a Python function that finds the longest substring of a 
given string that contains exactly K unique characters. 
If no such substring exists, return 0.
'''
'''
   Constraints: 
   1) The string S will have at least one character and at most 10^6 characters.
   2) The integer K will be between 1 and the number of distinct characters in the string.
'''
def longest_substring_k_unique(s: str, k: int) -> int:
    if s == None or s=="":
        return 0
    maximum = -1
    for letter in range(len(s)):
        for pairing in range(letter+1, len(s) + 1):
            unique_letters = set(s[letter:pairing])
            if len(unique_letters) == k:
                maximum = max(maximum, pairing - letter)
    return maximum
                
#Testing
### Example Input/Output:
'''
1. **Example 1**:
   ```
   Input: S = "araaci", K = 2
   Output: 4
   Explanation: The longest substring with exactly 2 unique characters is "araa".
   ```
'''
s = "araaci"
k = 2
print(longest_substring_k_unique(s,k))
'''
2. **Example 2**:
   ```
   Input: S = "cbbebi", K = 3
   Output: 5
   Explanation: The longest substring with exactly 3 unique characters is "cbbeb" or "bbebi".
   ```
'''
s = "cbbebi"
k = 3
print(longest_substring_k_unique(s,k))
'''
3. **Example 3**:
   ```
   Input: S = "aa", K = 1
   Output: 2
   Explanation: The longest substring with exactly 1 unique character is "aa".
'''
s = "aa"
k = 1
print(longest_substring_k_unique(s,k))

s = None
k = 3
print(longest_substring_k_unique(s,k))

s = ""
k = 2
print(longest_substring_k_unique(s,k))