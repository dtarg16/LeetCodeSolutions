class Solution:
    def makeGood(self, s: str) -> str:
        ss = []
        
        for c in s: 
            if ss and ss[-1] == c.swapcase():
                ss.pop()
            else: 
                ss.append(c)
        
        return "".join(ss)