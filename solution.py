def longest_substring_k_unique(s: str, k: int) -> int:
    retCount = 0
    charCount = 0
    arr = []
    for char in s:
        if char not in arr:
            if charCount !=k:
                retCount = retCount + 1
                charCount = charCount + 1
                arr.append(char)
        else:
            retCount = retCount + 1
    return retCount
