def longest_substring_k_unique(s: str, k: int) -> int:
    # Check string length
    if (len(s) < 1 or len(s)  > 10**6):
        raise ValueError("The string 's' most have at least one character and at most 10^6 characters.")
    
    # Check 'k'
    check_distinct_chars = len(set(s))
    if (k < 1 or k > check_distinct_chars):
        raise ValueError("The integer 'k' must be between 1 and the number of distinct characters in the string.")

    left = 0
    max_length = 0
    list_of_unique_chars = {}

    for right in range(len(s)):
        # Add the character to the list
        if s[right] not in list_of_unique_chars:
            list_of_unique_chars[s[right]] = 1
        else:
            list_of_unique_chars[s[right]] += 1
        
        # If the number of unique characters on the list exceeds k, remove from left
        while len(list_of_unique_chars) > k:
            list_of_unique_chars[s[left]] -= 1
            # Remove the character from the dictionary if its count becomes zero
            if list_of_unique_chars[s[left]] == 0:
                del list_of_unique_chars[s[left]]
            left += 1
        
        # Calculate the maximum length so far
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length

    return max_length

def main():
    try:
        result = longest_substring_k_unique('cbebbi', 3)
        print(result)
    except ValueError as ve:
        print(f"Input error: {ve}")

if __name__ == "__main__":
    main()