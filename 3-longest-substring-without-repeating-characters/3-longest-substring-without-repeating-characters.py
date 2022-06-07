class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxx = 0
        usedChar = {}
        
        for i in range(len(s)):
            ch = s[i]
            if ch in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxx = max(maxx, i - start + 1)

            usedChar[s[i]] = i

        return maxx