def longest_substring_k_unique(s: str, k: int) -> int:
    window = len(s)
    while window >= k:
        start = 0
        while start+window<=len(s):
            if check_window(s, start, k, window):
                return window
            start += 1
        window -= 1
    return 0
    
def check_window(s: str, start: int, k: int, length: int) -> int:
    uniqueChars = []
    for x in s[start:(start+length)]:
        if not x in uniqueChars:
            uniqueChars.append(x)
    return len(uniqueChars) == k
