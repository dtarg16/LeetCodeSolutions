class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = ord('A')
        if len(columnTitle) == 1:
            return ord(columnTitle[0]) - base + 1
        
        return self.titleToNumber(columnTitle[:-1]) * 26 +  ord(columnTitle[-1]) - base + 1