def longest_substring_k_unique(s, k):
    n = len(s)
    if n == 0 or k == 0:
        return -1

    char_count = {}
    left = 0
    answer = -1

    for right in range(n):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        if len(char_count) == k:
            answer = max(answer, right - left + 1)
    print(answer)
    return answer


s1 = "araaci"
s2 = "cbbebi"
s3 = "aa"


# Testing
longest_substring_k_unique(s1, 3)
longest_substring_k_unique(s2, 2)
longest_substring_k_unique(s3, 1)
