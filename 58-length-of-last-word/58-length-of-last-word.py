class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s) - 1
        
        while right > 0 and s[right] == " ":
            right -= 1
            
        left = right
        
        while left >= 0 and s[left] != " ":
            left -= 1
            
        return right - left