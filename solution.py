def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    length = len(s)
    result = 0
    
    for i in range(length):
        for j in range(i + 1, length + 1):
            # Adds distinct (unique) values from string
            distinct = set(s[i:j])
            if len(distinct) > k:
                break
            else:
                result = max(result, j - i)
    return result


print(longest_substring_k_unique("araaci", 2))
print(longest_substring_k_unique("cbbebi", 3))
print(longest_substring_k_unique("aa", 1))