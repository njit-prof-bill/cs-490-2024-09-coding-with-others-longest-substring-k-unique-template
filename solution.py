def longest_substring_k_unique(s: str, k: int) -> int:
    print("Input S = \"" + s + "\", K = " + str(k))
    largest=0
    answer=[]
    for i in range(len(s)):
        letters=[]
        st=""
        letters.append(s[i])
        st+=(s[i])
        count=1
        j=i+1
        while j<len(s):
            if s[j] in letters:
                count+=1
                st+=(s[j])
                j+=1

            elif len(letters)<k:
                letters.append(s[j])
                count+=1
                st+=(s[j])
                j+=1

            else:    
                break

        if count > largest and len(letters)==k:
            largest=count
            answer=[]
            answer.append(st)
            
        elif count == largest and len(letters)==k:
            answer.append(st)
        
    if largest==0:
        print("No substring with exactly " + str(k) + " unique characters.")
        return 0
    else:
        print("Output: " + str(largest))
        if len(answer)>1:
            print("Explanation: The longest substring with exactly " + str(k) + " unique characters is \"" +  ", ".join(answer[:-1]) + "\" and \"" + answer[-1] + "\".")
        else:
            print("Explanation: The longest substring with exactly " + str(k) + " unique characters is \"" +  "".join(answer) + "\".")
        return largest
            
#longest_substring_k_unique("araaci", 2)
#longest_substring_k_unique("cbbebi", 3)
#longest_substring_k_unique("aa", 1)
#longest_substring_k_unique("aa", 2)
    
                
   