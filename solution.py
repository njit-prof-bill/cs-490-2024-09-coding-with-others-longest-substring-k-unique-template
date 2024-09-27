def longest_substring_k_unique(s: str, k: int) -> int:
    start = 0
    end = 0
    dict = {}
    maximum = 0
    while end < len(s):
        dict[s[end]] = dict.get(s[end], 0) + 1
        if len(dict) < k:
            end += 1
        elif len(dict) == k:
            if maximum < end - start + 1:
                maximum = end - start + 1
            end += 1
        elif len(dict) > k:
            while len(dict) > k:
                dict[s[start]] -= 1
                if dict[s[start]] == 0:
                    del dict[s[start]]
                start += 1
            end += 1
    return maximum

print(longest_substring_k_unique("araaci", 2))
print(longest_substring_k_unique("cbbebi", 3))
print(longest_substring_k_unique("aa", 1))




