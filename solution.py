def longest_substring_k_unique(s: str, k: int) -> int:
    result = ""
    unique_count = 0
    for char in s:
        if char not in result and unique_count < k:
            unique_count+=1
            result += char
        elif char in result:
            result += char

    if unique_count < k:
        result = ""

    
    return len(result)


res = longest_substring_k_unique("aa",1)
print(res)
