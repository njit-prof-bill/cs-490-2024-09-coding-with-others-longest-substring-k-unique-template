def longest_substring_k_unique(s: str, k: int) -> int:
   subs = ""
   char = ''
   if k > len(s):
       return 0
   max, ind, curind = "", 0, 0
   for i in range(len(s)):
       if len(char) < k:
           subs += s[i]
           char += s[i]
           continue
       elif s[i] in char:
           subs += s[i]
       else:
           if len(subs) > len(max):
               max = subs
               ind = curind
           chars = ''
           subs += s[i]
           for j in range(len(subs)-1, 0, -1):
               if len(chars) == k and subs[j] not in chars:
                   subs = subs[j+1:]
                   break
               elif subs[j] not in chars:
                   chars += subs[j]
           curind = i
   if(len(subs) > len(max)):
       max = subs
   return len(max)


