def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    if len(s) == 0:
        return 0
    answer = 0
    front = 0
    back = 0
    chars = {}
    while back < len(s):
        if s[back] in chars:
            chars[s[back]] +=1
        else:
            chars[s[back]] = 1

        while len(chars)>k:
            chars[s[front]] -=1
            if chars[s[front]] == 0:
                del chars[s[front]]
            front +=1

        answer = max(answer, back-front +1)
        back+=1

    return answer

