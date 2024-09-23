def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    longest = [""]
    for start in range(len(s)+1):
        for end in range(start+1,len(s)+1):
            substr = s[start:end]
            substrDict = {i: substr.count(i) for i in set(substr)}
            if (len(substrDict) == k):
                if (len(substr) > len(longest[0])):
                    longest = [substr]
                elif (len(substr) == len(longest[0])):
                    longest.append(substr)
    return longest

tests = [("araaci", 2), ("cbbebi", 3), ("aa", 1)]
for test in tests:
    longestSubstring = longest_substring_k_unique(test[0], test[1])
    print(f"\nInput: S = {test[0]}, K = {test[1]}\n"
        f"Output: {len(longestSubstring[0])}\n"
        f"Longest Substrings: {', '.join(longestSubstring)}")