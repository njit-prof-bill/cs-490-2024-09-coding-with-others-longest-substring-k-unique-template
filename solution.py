# return the string thats longer
def longer(s1: str, s2: str) -> str:
	if(s2 is None):
		return s1
	if(s1 is None):
		return s2
	return s1 if len(s1) > len(s2) else s2

# returns true if string s has k unique elements
def has_k_unique(s: str, k: int) -> bool:
	unique = set()
	for c in s:
		if(c in unique):
			continue
		unique.add(c)
		if(len(unique) > k):
			return False
	return len(unique) == k

# find the length of the longest substring of s that contains k unique characters
def longest_substring_k_unique(s: str, k: int) -> int:
	max: str = None
	for length in range(k, len(s)+1):
		for i in range(len(s)-length+1):
			substr = s[i:length+i+1]
			if(has_k_unique(substr, k)):
				max = longer(max, substr)
	return 0 if max is None else len(max)
