def longest_substring_k_unique(s: str, k: int) -> int:
    '''Finds the longest substring of a given string s that contains exactly k unique characters. If no such substring exists, 0 is returned'''

    # For length in possible lengths of substrings
    # Starts at longest length and goes to smalles
    # Iterates over list of lengths from length of string s to 1
    for length in reversed(range(1, len(s) + 1)):
         
        # Choose starting point
        # Iterates over list of possible starting points
        for start in range(len(s) - length + 1):
            
            # Find ending point with given length
            end = start + length

            # Build substring
            substring = s[start:end]

            # If the length of the set of unique characters in the substring equals k
            if (len(set(substring)) == k):
                # Return the length of the substring
                return length
            
    # If no substrings exist with k unique characters, return 0
    return 0