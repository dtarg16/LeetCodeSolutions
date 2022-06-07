class Solution:
    
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            tmp = self.longest_ss(s, i, i)
            if len(tmp) > len(res):
                res = tmp
                
            tmp = self.longest_ss(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
                
        return res

    
    def longest_ss(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
            
        return s[l+1:r]