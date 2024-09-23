def longest_substring_k_unique(s: str, k: int) -> int:
    ret_count = 0
    char_count = 0
    arr = []
    for char in s:
        if char not in arr:
            if char_count != k:
                ret_count = ret_count + 1
                char_count = char_count + 1
                arr.append(char)
        else:
            ret_count = ret_count + 1
    return ret_count