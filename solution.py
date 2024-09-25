#finding longest substring with k unique characters using two pointer method
def longest_substring_k_unique(s: str, k: int) -> tuple:
    char_count = { }
    i = -1 
    j = -1
    answer = -1
    substrings = []

    while True:
        #loop  through the string with the left pointer
        while i < len(s) - 1:
            i += 1
            character =  s[i]
            char_count[character]  = char_count.get(character, 0) + 1

            # if the number of unique characters is greater than k, move the right pointer to the left
            if len(char_count) < k:
                continue

            #  if the number of unique characters is equal to k, calculate result
            elif len(char_count) == k:
                result = i - j
                #  if the length of the current substring is greater than the answer, update the answer
                if  result > answer:
                    answer = result
                    substrings = [s[j+1:i+1]]
                #   if the length of the current substring is equal to the answer, add it to the list of
                elif  result == answer:
                    substrings.append(s[j+1:i+1])
            else:
                break

        #   if the number of unique characters is greater than k, move the right pointer to the left
        while j < i:
            j += 1
            character = s[j]

            #  if the number of unique characters is greater than k, move the right pointer to the left
            if char_count[character] == 1:
                del  char_count[character]
            else:
                char_count[character] -= 1
            
            #   if the number of unique characters is equal to k, calculate result
            if len(char_count) == k:
                result = i - j
                #   if the length of the current substring is greater than the answer, update the answer
                if result > answer:
                    answer = result
                    substrings = [s[j+1:i+1]]
                    #   if the length of the current substring is equal to the answer, add it to the list
                elif  result == answer:
                    substrings.append(s[j+1:i+1])
                break
            elif len(char_count) > k:
                continue

            if answer ==  -1:
                return 0, " "

        return answer, substrings

#driver function
def main():
    s = input("Input: Enter string: ")
    k_input = input("Input: Enter k: ")

#error handling
    try:
        if not k_input.isdigit():
            raise ValueError("Input k is not a digit")
        if len(s) == 0:
            raise ValueError("Check Again: Must enter at least one character for valid string entry.")
        
        k = int(k_input)

        if k < 1 or k > len(s):
            raise ValueError("Check Again: k must be between 1 and the length of the string.")
    except  ValueError as e:
        print(f"Value Error: {e}")
        return

#function call
    length, substring = longest_substring_k_unique(s,k)

#print results
    if length > 0:
        print("Output: ", length)
        print("Explanation: The longest substring with exactly ",  k, " unique characters is: ",  substring)
    else:
        print("Output: 0")
        print("Explanation: No substring with exactly ",  k, " unique characters exists.")

if __name__  == "__main__":
    main()


