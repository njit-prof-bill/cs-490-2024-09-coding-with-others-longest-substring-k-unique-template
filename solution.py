def longest_substring_k_unique(s: str, k: int) -> int:
    n = len(s) # length of the string
    if n * k == 0:  # Check for empty string
        return 0  # If either is true, return 0

    start = 0  # start pointer
    max_length = 0  # max length
    char_count = {}  # Dictionary to count occurrences of characters
    unique = 0  # Counter for unique characters

    for i in range(n):
        if s[i] not in char_count:
            unique += 1  # Increment unique character count
            char_count[s[i]] = 0  # start the count for the new character
        char_count[s[i]] += 1  # Increment the count of the character

        # Reduce the window to keep exactly k unique characters
        while unique > k:
            start_char = s[start]
            char_count[start_char] -= 1  # Decrement count
            if char_count[start_char ] == 0:
                unique -= 1  # Decrement unique character count
                del char_count[start_char]  # Remove the character from the dictionary
            start += 1  # Move the start pointer to the right

        # Update max_length for exactly k unique characters
        if unique == k:
            max_length = max(max_length, i - start + 1)

    return max_length  # Return the length



#Test cases
length = longest_substring_k_unique("araaci", 2)
print(f"Length: {length}")  # Output: Length: 4
length = longest_substring_k_unique("cbbebi" ,3)
print(f"Length: : {length}")
length = longest_substring_k_unique("aa",1)
print(f"Length: : {length}")
length = longest_substring_k_unique("aaaaaa",2)
print(f"Length: : {length}")
length = longest_substring_k_unique("aaaaaabbbbbb",4)
print(f"Length: : {length}")
length = longest_substring_k_unique("aaaaaabbbbbbcdaaaaaaaaa",3)
print(f"Length: : {length}")
