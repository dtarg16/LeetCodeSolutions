class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([ch for ch in s if 'a' <= ch <= 'z' or '0' <= ch <= '9'])
        return s == s[::-1]