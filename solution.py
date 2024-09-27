def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here
    variations = []
    curr_letter = s[0]
    changes = 0
    curr_str = ""
    for letter in s:
        if letter == curr_letter:
            curr_str += letter
            continue
        elif changes == k or len(curr_str) == len(s):
            variations.append(curr_str)
            changes = 0
            curr_str = ""
            break
        else:
            curr_str += letter
            curr_letter = letter
            changes += 1
            continue
    if curr_str not in variations and curr_str != "":
        variations.append(curr_str)

    sorted_var = sorted(variations, key=lambda x: len(x))
    print(sorted_var[-1])
    pass


if __name__ == "__main__":
    longest_substring_k_unique("araaci", 2)
    longest_substring_k_unique("cbbebi", 3)
    longest_substring_k_unique("aa", 1)
