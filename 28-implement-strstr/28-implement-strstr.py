class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        ans = -1
        for i in range(len(haystack) - len(needle) + 1):
            s = haystack[i:i + len(needle)]
            if s == needle:
                ans = i
                break
        return ans
