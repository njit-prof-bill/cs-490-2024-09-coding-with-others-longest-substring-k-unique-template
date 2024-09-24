def longest_substring_k_unique(s: str, k: int) -> int:
    n = len(s)
    cnt = [0] * 26
    i = j = m = res = 0
    while j < n:
        if m <= k:
            idx = ord(s[j])-ord('a')
            if cnt[idx] == 0:
                m += 1
            cnt[idx] += 1
            j += 1
            if m == k:
                res = max(res, j - i)
        else:
            idx = ord(s[i])-ord('a')
            cnt[idx] -= 1
            if cnt[idx] == 0:
                m -= 1
            i += 1
    return res
    
