def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    counts = {}
    res = 0
    uniq_count = 0
    left = 0

    for right in range(len(s)):
        rchar = s[right]
        if rchar not in counts or counts[rchar] == 0:
            counts[rchar] = 1
            uniq_count += 1
        else:
            counts[rchar] += 1

        while uniq_count > k:
            lchar = s[left]
            counts[lchar] -= 1
            if counts[lchar] == 0:
                uniq_count -= 1
            left += 1

        if uniq_count == k:
            res = max(res, right - left + 1)

    return res