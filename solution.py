def longest_substring_k_unique(s: str, k: int) -> int:

    stringSize = len(s)
    finalAnswer = ""

    for i in range(stringSize):
        freq = set()
        answer = ""
        for j in range(i, stringSize):
            if s[j] in freq or len(freq) < k:
                answer += s[j]
                freq.add(s[j])
            else:
                break

        if len(finalAnswer) < len(answer) and len(freq) == k:
            finalAnswer = answer

    return len(finalAnswer)
