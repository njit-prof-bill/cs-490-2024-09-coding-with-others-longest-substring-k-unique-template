def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    # if (k==0 or str == "" ):
    #     print(f"K must be 1 or higher and the String must not be empty")
    #     return 0, []
    strLen = len(s)
    maxLen = 0
    substrings = []
    for i in range(strLen):
        dict = {}

        for j in range(i,strLen):
            dict[s[j]] = dict.get(s[j], 0) + 1
            if (len(dict)==k):
                currentLen = j-i+1
                if currentLen>maxLen:
                    maxLen = max(maxLen, currentLen)
                    substrings = [s[i:j + 1]]
                elif currentLen==maxLen:
                    substrings.append(s[i:j + 1])
            elif len(dict)>k:
                break
    return maxLen, substrings
# Test cases
# test_cases = [
#     ("cbbebi", 3),
#     ("araaci", 2),
#     ("aa", 1),
#     ("   ", 0),
#     ("a", 1),
#     ("abcdef", 6),
# ]

# # Run the test cases
# for s, k in test_cases:
#     length, substrings = longest_substring_k_unique(s, k)
#     if(length == 1):
#         print(f"Input: S = '{s}', K = '{k}'\nOutput: '{length}'\nExplanation: The longest substring with exactly '{k}' unique character is '{substrings}'" )
#     else:
#         print(f"Input: S = '{s}', K = '{k}'\nOutput: '{length}'\nExplanation: The longest substring with exactly '{k}' unique characters is '{substrings}'" )

while True:
    # use for this command winpty python solution.py for git bash terminal
    # for some reason when running just python solution.py it doesn't go to the k input
    #print("Before input")
    s = input("Enter a string: ")
    #print("After input")
    k = int(input("Enter the K number of unique characters: "))

    length, substrings = longest_substring_k_unique(s, k)
    
    if length == 0 and (k <= 0 or s == ""):
        print(f"Input: S = '{s}', K = '{k}'\nOutput: '{length}'\nExplanation: K must be 1 or higher and the string must not be empty.")
    elif length == 1:
        print(f"Input: S = '{s}', K = '{k}'\nOutput: '{length}'\nExplanation: The longest substring with exactly '{k}' unique character is '{substrings}'")
    else:
        print(f"Input: S = '{s}', K = '{k}'\nOutput: '{length}'\nExplanation: The longest substring with exactly '{k}' unique characters is '{substrings}'")

