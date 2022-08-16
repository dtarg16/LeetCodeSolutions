from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        
        for i in range(len(s)):
            ch = s[i]
            if counter[ch] == 1:
                return i
            
        return -1