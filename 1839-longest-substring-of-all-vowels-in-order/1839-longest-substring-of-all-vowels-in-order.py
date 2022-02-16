class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        pos = 0
        ans = 0
        count = 0
        vowel = 'aeiou'
        
        for i in range(n):
            ch = word[i]
            if pos != 0 and ch == vowel[pos-1]:
                count += 1
            elif pos < 5 and ch == vowel[pos]:
                count += 1
                pos += 1
            else:
                pos = 0
                count = 0
                if ch == 'a':
                    count = 1
                    pos = 1
            if pos == 5:
                ans = max(ans, count)
        return ans
            
        