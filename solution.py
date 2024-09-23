import unittest

def longest_substring_k_unique(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0
    
    L, R = 0, 0
    res = 0
    chars = {}

    while R < len(s):
        chars[s[R]] = chars.get(s[R], 0) + 1

        while len(chars) > k:
            chars[s[L]] -= 1
            if chars[s[L]] == 0:
                del chars[s[L]]
            L += 1

        if len(chars) == k:
            res = max(res, R - L + 1)
        
        R += 1
    
    return res

class TestLongestSubstringWithKUniqueChars(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(longest_substring_k_unique("araaci", 2), 4)
        self.assertEqual(longest_substring_k_unique("araaci", 1), 2)
        self.assertEqual(longest_substring_k_unique("cbbebi", 3), 5)

    def test_no_such_substring(self):
        self.assertEqual(longest_substring_k_unique("abc", 4), 0)
        self.assertEqual(longest_substring_k_unique("abc", 0), 0)

    def test_edge_cases(self):
        self.assertEqual(longest_substring_k_unique("", 2), 0)
        self.assertEqual(longest_substring_k_unique("a", 1), 1)
        self.assertEqual(longest_substring_k_unique("a", 2), 0)

    def test_entire_string_is_valid(self):
        self.assertEqual(longest_substring_k_unique("abcabcabc", 3), 9)
        self.assertEqual(longest_substring_k_unique("aabbcc", 2), 4)

    def test_crazy(self):
        self.assertEqual(longest_substring_k_unique("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 2), 0)

if __name__ == "__main__":
    unittest.main()