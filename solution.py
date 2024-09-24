def longest_substring_k_unique(s: str, k: int) -> int:
    # Write your code here

    letters=[] #document occuring letters
    max_length=0 #maximum length of string that fits the requirements

    if len(s) <k: #can't have string less than k unique characters
        return 0

    length=0 #current length of substr
    for i in range (len(s)-k): #looping through the string to find max substring
        j=0 #incrementing by one, looking at the next character
        while len(letters)<=k: #k unique characters not reached
            if i+j >= len(s): #end of string
                if len(letters) < k and max_length==0: #unique characters in entire string is less than k
                    return 0
                break
            
            if s[i+j] not in letters: #next potential unique letter
                letters.append(s[i+j]) 
                if len(letters) > k: #exceeds k unqiue letters
                    break
            length= length+1 #increment substr length by one
            j= j+1 #next character
        
        if length > max_length: #maximum substr so far
            max_length= length

        #resset for next iteration
        length=0
        letters=[]
    
    return max_length

#Test cases
print(longest_substring_k_unique("aaaai",2))
print(longest_substring_k_unique("cbbebiasdfgbhw",3))
print(longest_substring_k_unique("aaabaaaba",1))